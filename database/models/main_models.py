from database.models.base_model import BaseModel
from database.models.database_init import db


class CardsCollection(BaseModel, db.Model):
    __tablename__ = 'CardsCollection'
    collectionID = db.Column(db.Integer, primary_key=True)
    collectionName = db.Column(db.String)
    collectionDescription = db.Column(db.JSON)
    holderID = db.Column(db.Integer, db.ForeignKey('User.userID'), nullable=False)
    cardInfo = db.relationship('UserCollectionInfo', backref='cardsCollection', lazy=True)
    cards = db.relationship('Card', backref='cardsCollection', lazy=True)


class Card(BaseModel):
    __tablename__ = 'Card'
    cardID = db.Column(db.Integer, primary_key=True)
    collectionID = db.Column(db.Integer, db.ForeignKey('CardsCollection.collectionID'), nullable=False)
    cardInside = db.Column(db.JSON)


class User(BaseModel):
    __tablename__ = 'User'
    userID = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String)
    userPasswordHash = db.Column(db.String)
    userInfo = db.Column(db.JSON)
    cards = db.relationship('CardsCollection', backref='user', lazy=True)
    cardsWatched = db.relationship('CardWatched', backref='user', lazy=True)


class UserCollectionInfo(BaseModel, db.Model):
    __tablename__ = 'UserCollectionInfo'
    userID = db.Column(db.Integer, db.ForeignKey('User.userID'), primary_key=True, )
    collectionID = db.Column(db.Integer, db.ForeignKey('CardsCollection.collectionID'), primary_key=True)
    userCardInfo = db.Column(db.JSON)


class CardWatched(BaseModel):
    __tablename__ = 'CardWatched'
    cardWatchedID = db.Column(db.Integer, primary_key=True)
    cardID = db.Column(db.Integer, db.ForeignKey('Card.cardID'), primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('User.userID'))


def init_models():
    pass
