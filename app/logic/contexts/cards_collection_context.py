import logging

from app.database import Session
from app.database.models.main_models import CardsCollection, Card
from app.logic.contexts.card_inside import CardInside


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
    def get_single_card_by_id(card_id: int):
        card = Session.query(Card) \
            .filter(Card.cardID == card_id) \
            .first()
        return card \
            if card is not None else False

    @staticmethod
    def insert_inside_json_into_single_card(card: Card, card_inside: CardInside):
        card.cardInside = card_inside.json()
        Session.add_and_commit(card)
        return card_inside is not None