from flask_login import UserMixin

from app.database.models.base_model import BaseModel
from app.database.models.database_init import db


class CardsCollection(BaseModel, db.Model):
    __tablename__ = 'CardsCollection'
    cardID = db.Column(db.Integer, primary_key=True)
    collectionName = db.Column(db.String)
    collectionDescription = db.Column(db.String)
    holderID = db.Column(db.Integer, db.ForeignKey('User.userID'), nullable=False)
    cardInfo = db.relationship('UserCardInfo', backref='cardsCollection', lazy=True)
    singleCards = db.relationship('Card', backref='cardsCollection', lazy=True)


class Card(BaseModel):
    __tablename__ = 'Card'
    cardID = db.Column(db.Integer, primary_key=True)
    collectionID = db.Column(db.Integer, db.ForeignKey('CardsCollection.cardID'), nullable=False)
    cardInside = db.Column(db.String)


class User(BaseModel):
    __tablename__ = 'User'
    userID = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String, unique=True)
    userEmail = db.Column(db.String, unique=True)
    userPasswordHash = db.Column(db.String)
    userInfo = db.Column(db.JSON)
    cards = db.relationship('CardsCollection', backref='user', lazy=True)

    def is_authenticated(self) -> bool:
        return False

    def is_active(self) -> bool:
        return True

    def is_anonymous(self) -> bool:
        return False

    def get_id(self) -> str:
        return self.userEmail


class UserCardInfo(BaseModel, db.Model):
    __tablename__ = 'UserCardInfo'
    userID = db.Column(db.Integer, db.ForeignKey('User.userID'), primary_key=True, )
    cardID = db.Column(db.Integer, db.ForeignKey('CardsCollection.cardID'), primary_key=True)
    userCardInfo = db.Column(db.String)


def init_models():
    pass
