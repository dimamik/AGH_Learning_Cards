from database.models.main_models import Card, User, CardWatched
from database.session import Session
from logic.contexts.base_context import BaseContext
from logic.contexts.card_inside import CardInside


class CardContext(BaseContext):
    def __init__(self, collection, card=None, card_inside=None):
        super(CardContext, self).__init__()
        if card is None:
            if card_inside is None:
                card = Card()
                card_inside = CardInside()
                card.cardsCollection = collection
            card.cardInside = card_inside.json()
            Session.add_and_commit(card)
        self.instance = card

    def change_card_inside(self, new_inside: dict) -> bool:
        if new_inside:
            self.instance.cardInside = new_inside
            Session.commit()
        return new_inside is not None

    def add_card_to_watched(self, user: User):
        if user in User.query.all():
            card_watched = CardWatched()
            card_watched.cardID = self.instance.cardID
            card_watched.userID = user.userID
            Session.add_and_commit(card_watched)
