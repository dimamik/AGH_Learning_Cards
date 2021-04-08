from flask import Flask

from database.models.database_init import regenerate_database_with_app
from env import POSTGRES
from logic.contexts.cards_collection_context import CardsCollectionContext

app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


def init_app():
    app.app_context().push()
    regenerate_database_with_app(app)


def test():
    # usr = UserContext.get_user_instance_by_username('username')
    # cardCollInstance = CardsCollectionContext(usr.user)
    # cardCollInstance = CardsCollectionContext.get_collection_by_id(6)
    # cardCollInstance.add_single_card_to_collection()
    card = CardsCollectionContext.get_single_card_by_id(2)
    d = {'front': "Word to learn", 'back': 'Definition of the word to learn'}
    CardsCollectionContext.insert_inside_json_into_single_card(card, d)
    # print(cardCollInstance.cards.singleCards[0])
    # print(cardCollInstance.cards.singleCards)
    # print(cardCollInstance.cards)


if __name__ == '__main__':
    init_app()
    test()
