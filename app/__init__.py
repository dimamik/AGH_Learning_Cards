from flask import Flask

from app.database.models.main_models import User
from app.logic.contexts.user_context import UserContext
from app.routes import HTTP_NO_CONTENT, HTTP_UNAUTH, HTTP_NOT_FOUND, HTTP_BAD_REQ, HTTP_CONFLICT
from config import POSTGRES, SECRET_KEY


def create_app():
    app = Flask(__name__)

    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES["user"]}:{POSTGRES["pw"]}@{POSTGRES["host"]}: \
            {POSTGRES["port"]}/{POSTGRES["db"]}'
    app.secret_key = SECRET_KEY

    from app.database.models.database_init import db
    from app.auth import argon2
    from app.auth import login_manager

    db.init_app(app)
    argon2.init_app(app)
    login_manager.init_app(app)

    app.app_context().push()

    db.create_all()

    from app.routes import router

    app.register_blueprint(router)

    return app


