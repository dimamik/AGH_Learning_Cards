import flask
from flask import Blueprint, request
from flask_cors import CORS, cross_origin
from flask_login import login_required, current_user

from app.http.errors import HttpException
from app.http.http_statuses import HTTP_CREATED, HTTP_OK, HTTP_NO_CONTENT, HTTP_UNAUTHORIZED
from app.http.transfer_objects import UserCreationRequest, UserLoginRequest
from app.logic.contexts.card_context import CardContext
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


@router.route('/collections/user/<user_id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def all_collections_by_user(user_id):
    to_ret = flask.jsonify(CardsCollectionContext.get_user_collections_json(user_id))
    if to_ret is not None:
        return to_ret, HTTP_OK


@router.route('/collections/<collection_id>', methods=['GET'])
@login_required
@cross_origin(supports_credentials=True)
def get_cards_in_collection(collection_id):
    user_id = current_user.instance.userID
    to_ret = flask.jsonify(
        CardsCollectionContext.get_cards_in_collection_with_respect_to_watched(collection_id, user_id))

    if to_ret is not None:
        return to_ret, HTTP_OK


@router.route('/current-user/collections', methods=['POST'])
@cross_origin(supports_credentials=True)
@login_required
def add_new_collection():
    user_id = current_user.instance.userID
    new_collection_id = CardsCollectionContext.add_new_collection(holder_id=user_id)
    collection = CardsCollectionContext(
        CardsCollectionContext.get_collection_by_id(collection_id=new_collection_id)
    )
    collection.set_description(request.json['collectionDescription'])
    collection.set_name(request.json['collectionName'])
    return flask.jsonify(new_collection_id), HTTP_OK


@router.route('/current-user/collections', methods=['DELETE'])
@cross_origin(supports_credentials=True)
@login_required
def delete_collection():
    collection_id = request.json['collection_id']
    if collection_id is not None:
        owner_of_collection = CardsCollectionContext.get_collection_by_id(collection_id)
        if owner_of_collection.holderID == current_user.instance.userID:
            CardsCollectionContext.delete_collection(collection_id)
            return "", HTTP_OK
    return flask.jsonify("Unauthorized"), HTTP_UNAUTHORIZED


@router.route('/current-user/favorite', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_user_favorite():
    user_id = current_user.instance.userID
    usr_fav = CardsCollectionContext.get_user_favorites(user_id)
    return flask.jsonify(usr_fav)


@router.route('/current-user/favorite/<collection_id>', methods=['POST'])
@cross_origin(supports_credentials=True)
@login_required
def add_to_user_favorite(collection_id):
    user_id = current_user.instance.userID
    try:
        CardsCollectionContext.add_to_user_favorite(user_id=user_id, collection_id=collection_id)
        return "", HTTP_OK
    except Exception as e:
        # TODO Don't send server errors to client TO REFACTOR
        return flask.jsonify(message=f'{e}'), 500


@router.route('/current-user/favorite/<collection_id>', methods=['DELETE'])
@cross_origin(supports_credentials=True)
@login_required
def delete_from_user_favorite(collection_id):
    user_id = current_user.instance.userID
    try:
        CardsCollectionContext.delete_from_user_favorite(user_id=user_id, collection_id=collection_id)
        return " ", HTTP_OK
    except Exception as e:
        # TODO Don't send server errors to client TO REFACTOR
        return flask.jsonify(message=f'{e}'), 500


@router.route('/collections/<collection_id>', methods=['POST'])
@cross_origin(supports_credentials=True)
@login_required
def add_card_to_collection(collection_id):
    user_id = current_user.instance.userID
    collection_instance = CardsCollectionContext.get_collection_by_id(collection_id)
    if user_id == collection_instance.holderID:
        collection_instance = CardsCollectionContext(collection_instance)
        single_card = CardContext(collection_instance.instance)
        single_card.change_card_inside(request.json['cardInside'])
        collection_instance.add_single_card_to_collection(single_card.instance)
        return "", HTTP_OK
    else:
        return "Unauthorized", HTTP_UNAUTHORIZED


@router.route('/collections/<collection_id>', methods=['DELETE'])
@cross_origin(supports_credentials=True)
@login_required
def delete_card_from_collection(collection_id):
    user_id = current_user.instance.userID
    collection_instance = CardsCollectionContext.get_collection_by_id(collection_id)
    if user_id == collection_instance.holderID:
        CardsCollectionContext.delete_single_card_from_collection(request.json['cardID'])
        return "", HTTP_OK
    else:
        return "Unauthorized", HTTP_UNAUTHORIZED
