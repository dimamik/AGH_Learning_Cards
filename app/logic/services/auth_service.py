import re

import flask_login
from flask_argon2 import Argon2
from flask_login import LoginManager

from app.http.errors import BadRequestException, ConflictException, NotFoundException, UnauthorizedException
from app.http.transfer_objects import UserCreationRequest, UserResponse, UserLoginRequest
from app.logic.contexts.user_context import UserContext

argon2 = Argon2()
login_manager = LoginManager()

name_regex = re.compile('^\\w{3,16}$')
email_regex = re.compile("^.{1,50}@.{1,25}\\..{1,25}$")


def create_user(user_request: UserCreationRequest) -> UserResponse:
    _validate_username(user_request.user_name)
    _validate_email(user_request.user_email)
    _validate_password(user_request.user_password)

    if UserContext.exists_by_username(user_request.user_name):
        raise ConflictException("Username is already taken")
    elif UserContext.exists_by_email(user_request.user_email):
        raise ConflictException("Email is already taken")

    user_context = UserContext.add_new_user(
        user_request.user_name,
        user_request.user_email,
        argon2.generate_password_hash(user_request.user_password)
    )

    flask_login.login_user(user_context, remember=True)

    return UserResponse(user_context)


def login_user(user_request: UserLoginRequest) -> UserResponse:
    _validate_email(user_request.user_email)
    _validate_password(user_request.user_password)

    user_context = UserContext.get_user_instance_by_email(user_request.user_email)

    if user_context is None:
        raise NotFoundException("User with given email does not exist")
    elif not argon2.check_password_hash(user_context.instance.userPasswordHash, user_request.user_password):
        raise UnauthorizedException("Password is wrong")

    flask_login.login_user(user_context, remember=True)

    return UserResponse(user_context)


def logout_user():
    flask_login.logout_user()


def _validate_username(name: str):
    if not name:
        raise BadRequestException("Username is empty")
    elif not name_regex.match(name):
        raise BadRequestException("Username has wrong format")


def _validate_email(email: str):
    if not email:
        raise BadRequestException("Email is empty")
    elif not email_regex.match(email):
        raise BadRequestException("Email has wrong format")


def _validate_password(password: str):
    if not password:
        raise BadRequestException("Password is empty")
    elif len(password) < 7 or len(password) > 75:
        raise BadRequestException("Password has wrong format")


@login_manager.user_loader
def load_user(email):
    return UserContext.get_user_instance_by_email(email) if email else None
