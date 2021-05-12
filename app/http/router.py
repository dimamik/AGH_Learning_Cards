import flask
from flask import Blueprint, request
from flask_cors import CORS, cross_origin
from flask_login import login_required, current_user

from app.http.errors import HttpException
from app.http.http_statuses import HTTP_CREATED, HTTP_OK, HTTP_NO_CONTENT
from app.http.transfer_objects import UserCreationRequest, UserLoginRequest
from app.logic.contexts.cards_collection_context import CardsCollectionContext
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


@router.route('/auth/current-user', methods=['GET'])
@cross_origin(supports_credentials=True)
def handle_current():
    if current_user.is_anonymous:
        return flask.jsonify(''), HTTP_NO_CONTENT
    else:
        resp: dict = current_user.json()
        resp.pop('userPasswordHash')
        return flask.jsonify(resp), HTTP_OK


@router.route('/collections', methods=['GET'])
@cross_origin(supports_credentials=True)
def all_collections():
    return flask.jsonify(CardsCollectionContext.get_all_collections_json()), HTTP_OK


@router.route('/collections/<user_id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def all_collections_by_user(user_id):
    to_ret = flask.jsonify(CardsCollectionContext.get_user_collections_json(user_id))
    if to_ret is not None:
        return to_ret, HTTP_OK


@router.route('/collections/<user_id>/<collection_id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def all_single_collection_id(user_id, collection_id):
    to_ret = flask.jsonify(CardsCollectionContext.get_collection_by_id_json(collection_id))
    if to_ret is not None:
        return to_ret, HTTP_OK


@router.route('/collections/<user_id>/<collection_id>/cards', methods=['GET'])
@cross_origin(supports_credentials=True)
def all_cards_in_collection_id(user_id, collection_id):
    to_ret = flask.jsonify(str(CardsCollectionContext.get_single_cards_string_list(collection_id)))
    if to_ret is not None:
        return to_ret, HTTP_OK


@router.route('/current-user/collections', methods=['POST'])
@cross_origin(supports_credentials=True)
@login_required
def add_new_collection():
    # TODO Rethink the data flows
    print(CardsCollectionContext.add_new_collection(request.json['holder_id']))
    return "", HTTP_OK


@router.route('/current-user/collections', methods=['DELETE'])
@cross_origin(supports_credentials=True)
@login_required
def delete_collection():
    # TODO Delete Process
    return "", HTTP_OK


@router.route('/current-user/favorite', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_user_favorite():
    # TODO
    return HTTP_NO_CONTENT


@router.route('/current-user/favorite/<collection_id>', methods=['POST'])
@cross_origin(supports_credentials=True)
def add_to_user_favorite(collection_id):
    # TODO
    return HTTP_NO_CONTENT


@router.route('/current-user/favorite/<collection_id>', methods=['DELETE'])
@cross_origin(supports_credentials=True)
def delete_from_user_favorite(collection_id):
    # TODO
    return HTTP_NO_CONTENT
