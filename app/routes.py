import json

import flask
from flask import Response, Blueprint
from flask_login import login_user

import app.auth as auth
from app.database.models.main_models import User
from app.logic.contexts.user_context import UserContext

HTTP_BAD_REQ = 400
HTTP_NOT_FOUND = 404
HTTP_UNAUTH = 401
HTTP_CONFLICT = 409

HTTP_NO_CONTENT = 204


router = Blueprint('router', __name__)


@router.route('/sign-in', methods=['POST'])
def sign_in():
    body = json.loads(flask.request.data)

    email: str = body['email']
    password: str = body['password']

    if not auth.validate_email_and_password(email, password):
        return Response(json.dumps(body), status=HTTP_BAD_REQ, mimetype='application/json')

    user = UserContext.get_user_by_email(email)
    if not user:
        return Response(json.dumps(body), status=HTTP_NOT_FOUND, mimetype='application/json')

    if not auth.verify_password(password, user.userPasswordHash):
        return Response(json.dumps(body), status=HTTP_UNAUTH, mimetype='application/json')

    login_user(user)

    return Response(status=HTTP_NO_CONTENT, mimetype='application/json')


@router.route('/sign-up', methods=['POST'])
def sign_up():
    body = json.loads(flask.request.data)

    name: str = body['name']
    email: str = body['email']
    password: str = body['password']

    if not auth.validate_name(name) or not auth.validate_email_and_password(email, password):
        return Response(json.dumps(body), status=HTTP_BAD_REQ, mimetype='application/json')

    if UserContext.get_user_by_name_or_email(name, email):
        return Response(json.dumps(body), status=HTTP_CONFLICT, mimetype='application/json')

    user = User()
    user.userName = name
    user.userEmail = email
    user.userPasswordHash = auth.create_hash(password)

    UserContext.add_new_user(user)

    login_user(user)

    return Response(status=HTTP_NO_CONTENT, mimetype='application/json')
