from database.models.base_model import BaseModel
from database.models.database_init import db


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
    userName = db.Column(db.String)
    userPasswordHash = db.Column(db.String)
    userInfo = db.Column(db.JSON)
    cards = db.relationship('CardsCollection', backref='user', lazy=True)


class UserCardInfo(BaseModel, db.Model):
    __tablename__ = 'UserCardInfo'
    userID = db.Column(db.Integer, db.ForeignKey('User.userID'), primary_key=True, )
    cardID = db.Column(db.Integer, db.ForeignKey('CardsCollection.cardID'), primary_key=True)
    userCardInfo = db.Column(db.String)


def init_models():
    pass
