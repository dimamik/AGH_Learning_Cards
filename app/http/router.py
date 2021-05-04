import flask
from flask import Blueprint
from flask_cors import CORS, cross_origin
from flask_login import login_required

from app.http.errors import HttpException
from app.http.http_statuses import HTTP_CREATED, HTTP_OK, HTTP_NO_CONTENT
from app.http.transfer_objects import UserCreationRequest, UserLoginRequest
from app.logic.services import auth_service

router = Blueprint('router', __name__)

cors = CORS()


@router.route('/auth/sign-up', methods=['POST'])
@cross_origin(supports_credentials=True)
def handle_sign_up():
    try:
        user_request = UserCreationRequest(flask.request.json)
        user_response = auth_service.create_user(user_request)
        return flask.jsonify(user_response.to_dict()), HTTP_CREATED
    except HttpException as e:
        return flask.jsonify(message=f'{e}'), e.status


@router.route('/auth/sign-in', methods=['POST'])
@cross_origin(supports_credentials=True)
def handle_sign_in():
    try:
        user_request = UserLoginRequest(flask.request.json)
        user_response = auth_service.login_user(user_request)
        return flask.jsonify(user_response.to_dict()), HTTP_OK
    except HttpException as e:
        return flask.jsonify(message=f'{e}'), e.status


@router.route('/auth/sign-out', methods=['POST'])
@cross_origin(supports_credentials=True)
@login_required
def handle_sign_out():
    try:
        auth_service.logout_user()
        return '', HTTP_NO_CONTENT
    except HttpException as e:
        return flask.jsonify(message=f'{e}'), e.status


@router.route('/test', methods=['GET'])
@cross_origin(supports_credentials=True)
@login_required
def handle_test():
    try:
        return flask.jsonify(message='Test message protected by login_required'), HTTP_OK
    except HttpException as e:
        return flask.jsonify(message=f'{e}'), e.status
