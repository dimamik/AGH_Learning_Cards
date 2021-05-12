import logging
from typing import Union

from app import UserContext
from app.database.models.main_models import CardsCollection, Card, CardWatched, UserLikedCollection
from app.database.session import Session
from app.logic.contexts.base_context import BaseContext
from app.logic.contexts.card_context import CardContext


class CardsCollectionContext(BaseContext):
    def __init__(self, collection=None, holder_instance=None):
        super(CardsCollectionContext, self).__init__()
        if collection is None:
            if holder_instance is not None:
                collection = CardsCollection()
                collection.user = holder_instance
                Session.add_and_commit(collection)
            else:
                logging.error("Can't create object without a ref")
        self.instance = collection

    def set_description(self, description: str):
        self.instance.collectionDescription = description
        Session.commit()

    @staticmethod
    def get_collection_by_id(collection_id: int):
        collection = Session.query(CardsCollection) \
            .filter(CardsCollection.collectionID == collection_id) \
            .first()
        return collection

    @staticmethod
    def get_collection_by_id_json(collection_id):
        collection = Session.query(CardsCollection) \
            .filter(CardsCollection.collectionID == collection_id) \
            .first()
        return collection.json() or None

    def add_single_card_to_collection(self, single_card=Card(), card_inside=None) -> bool:
        if single_card not in self.instance.cards:
            single_card.cardsCollection = self.instance
            if card_inside is not None:
                single_card.cardInside = card_inside
            Session.add_and_commit(single_card)
            return True
        return False

    @staticmethod
    def get_user_collections_json(user_id: int):
        to_ret_plain = Session.query(CardsCollection).filter(CardsCollection.holderID == user_id).all()
        if to_ret_plain is not None:
            for index, obj in enumerate(to_ret_plain):
                to_ret_plain[index] = obj.json()
        return to_ret_plain

    @staticmethod
    def get_collection_watched_only_json(user_id):
        collection = Session.query(Card).join(CardWatched) \
            .filter(Card.collectionID == self.instance.collectionID,
                    CardWatched.userID == user_id).all()
        for index,obj in collection:
            collection[index] = obj.json()
        return collection


    @staticmethod
    def get_single_card_by_id(card_id: int) -> Union[CardContext, bool]:
        card = Session.query(Card) \
            .filter(Card.cardID == card_id) \
            .first()
        return CardContext(card.collectionID, card) \
            if card is not None else False

    @staticmethod
    def get_user_liked_collections(user_id: int):
        user = UserContext.get_user_instance_by_id(user_id).instance
        return user.collectionsLiked

    def add_collection_to_liked(self, user_context):
        user_liked_collection = UserLikedCollection()
        user_liked_collection.collectionID = self.instance.collectionID
        user_liked_collection.userID = user_context.instance.userID
        Session.add_and_commit(user_liked_collection)

    # TODO Place it somewhere else :)
    @staticmethod
    def get_all_collections_json():
        to_ret_plain = Session.query(CardsCollection).all()
        for index, obj in enumerate(to_ret_plain):
            to_ret_plain[index] = obj.json()
        return to_ret_plain

    @staticmethod
    def get_single_cards_string_list(collection_id):
        cards = CardsCollectionContext.get_collection_by_id(collection_id)
        to_ret = None
        if cards is not None:
            to_ret = cards.cards
        return to_ret

    @staticmethod
    def add_new_collection(holder_id):
        holder = UserContext.get_user_instance_by_id(holder_id)
        print(holder)
        if holder is not None:
            cards_coll_context = CardsCollectionContext(holder_instance=holder.instance)
            print(cards_coll_context)
            return cards_coll_context.instance.collectionID
        else:
            return False

    @staticmethod
    def delete_collection(collection_id):
        # TODO
        return True
