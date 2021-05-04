from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


class Session:
    @staticmethod
    def add_and_commit(object_to_add: db.Model):
        db.session.add(object_to_add)
        db.session.commit()

    @staticmethod
    def commit():
        db.session.commit()

    @staticmethod
    def query(object_to_query: db.Model):
        return db.session.query(object_to_query)
