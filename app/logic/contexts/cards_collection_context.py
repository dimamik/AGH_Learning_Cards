import logging

from app.database.models import db
from app.database.models import CardsCollection, Card
from app.logic.json_formatter.to_json import JsonEncoder


class CardsCollectionContext:
    def __init__(self, cards_parent=None, holder_instance=None):
        if cards_parent is None:
            if holder_instance is not None:
                cards_parent = CardsCollection()
                cards_parent.user = holder_instance
                db.session.add(cards_parent)
                db.session.commit()
            else:
                logging.error("Can't create object without a ref")
        self.cards = cards_parent

    def set_description(self, description: str):
        self.cards.collectionDescription = description
        db.session.commit()

    @staticmethod
    def get_collection_by_id(collection_id: int):
        collection = db.session.query(CardsCollection) \
            .filter(CardsCollection.cardID == collection_id) \
            .first()
        return CardsCollectionContext(collection) \
            if collection is not None else False

    def add_single_card_to_collection(self, single_card=Card(), card_inside=None) -> bool:
        if single_card not in self.cards.singleCards:
            single_card.cardsCollection = self.cards
            if card_inside is not None:
                single_card.cardInside = card_inside
            db.session.add(single_card)
            db.session.commit()
            return True
        return False

    def get_single_cards_list(self):
        return self.cards.singleCards

    @staticmethod
    def get_single_card_by_id(card_id: int):
        card = db.session.query(Card) \
            .filter(Card.cardID == card_id) \
            .first()
        return card \
            if card is not None else False

    @staticmethod
    def insert_inside_json_into_single_card(card: Card, dict_to_insert: dict):
        card.cardInside = JsonEncoder.dict_to_json(dict_to_insert)
        db.session.add(card)
        db.session.commit()
