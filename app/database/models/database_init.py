from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_database_with_app(app):
    db.init_app(app)
