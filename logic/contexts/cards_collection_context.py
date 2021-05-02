import logging
from typing import Optional

from database.models.main_models import CardsCollection, Card, CardWatched, UserLikedCollection
from database.session import Session
from logic.contexts.user_context import UserContext


class CardsCollectionContext:
    def __init__(self, collection=None, holder_instance=None):
        if collection is None:
            if holder_instance is not None:
                collection = CardsCollection()
                collection.user = holder_instance
                Session.add_and_commit(collection)
            else:
                logging.error("Can't create object without a ref")
        self.collection = collection

    def __repr__(self):
        return self.collection.__repr__()

    def set_description(self, description: str):
        self.collection.collectionDescription = description
        Session.commit()

    @staticmethod
    def get_collection_by_id(collection_id: int):
        collection = Session.query(CardsCollection) \
            .filter(CardsCollection.collectionID == collection_id) \
            .first()
        return CardsCollectionContext(collection) \
            if collection is not None else False

    def add_single_card_to_collection(self, single_card=Card(), card_inside=None) -> bool:
        if single_card not in self.collection.singleCards:
            single_card.cardsCollection = self.collection
            if card_inside is not None:
                single_card.cardInside = card_inside
            Session.add_and_commit(single_card)
            return True
        return False

    def get_single_cards_list(self):
        return self.collection.cards

    def get_all_cards_json(self):
        return self.collection.cards

    @staticmethod
    def get_user_collections(user_id: int):
        return Session.query(CardsCollection).filter(CardsCollection.holderID == user_id).all()

    def get_collection_watched_only(self, user_id):
        return Session.query(Card).join(CardWatched) \
            .filter(Card.collectionID == self.collection.collectionID,
                    CardWatched.userID == user_id).all()

    @staticmethod
    def get_single_card_by_id(card_id: int) -> Optional[Card]:
        card = Session.query(Card) \
            .filter(Card.cardID == card_id) \
            .first()
        return card \
            if card is not None else False

    @staticmethod
    def get_user_liked_collections(user_id: int):
        user = UserContext.get_user_instance_by_id(user_id).user
        return user.collectionsLiked

    def add_collection_to_liked(self, user_context):
        user_liked_collection = UserLikedCollection()
        user_liked_collection.collectionID = self.collection.collectionID
        user_liked_collection.userID = user_context.user.userID
        Session.add_and_commit(user_liked_collection)
