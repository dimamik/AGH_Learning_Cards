from database.models.main_models import Card
from database.session import Session
from logic.contexts.card_inside import CardInside


class CardContext:
    def __init__(self, collection, card=None, card_inside=None):
        if card is None:
            if card_inside is None:
                card = Card()
                card_inside = CardInside()
                card.cardsCollection = collection
            card.cardInside = card_inside.json()
            Session.add_and_commit(card)
        self.card = card

