from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def init_database_with_app(app):
    db.init_app(app)


def regenerate_database_with_app(app):
    global db
    db = SQLAlchemy(app)
