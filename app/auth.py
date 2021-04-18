import re

from flask_argon2 import Argon2
from flask_login import LoginManager

from app.logic.contexts.user_context import UserContext

argon2 = Argon2()
login_manager = LoginManager()

nameRegex = re.compile('^\\w{3,16}$')


def validate_name(name: str) -> bool:
    if not name:
        return False

    if not nameRegex.match(name):
        return False

    return True


def validate_email_and_password(email: str, password: str) -> bool:
    if not email or not password:
        return False

    if email.find('@') == -1 or len(email) < 5 or len(email) > 75 or len(password) < 7 or len(password) > 75:
        return False

    return True


def create_hash(password: str) -> str:
    return argon2.generate_password_hash(password)


def verify_password(password: str, hash_from_db: str) -> bool:
    return argon2.check_password_hash(hash_from_db, password)


@login_manager.user_loader
def load_user(email):
    return UserContext.get_user_by_email(email) if email else None
