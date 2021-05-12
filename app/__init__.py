from flask import Flask

from app.database.models.main_models import User
from app.logic.contexts.user_context import UserContext
from config import POSTGRES, SECRET_KEY


def create_app():
    app = Flask(__name__)

    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES["user"]}:{POSTGRES["pw"]}@{POSTGRES["host"]}: \
            {POSTGRES["port"]}/{POSTGRES["db"]}'
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.secret_key = SECRET_KEY

    from app.database import db, migrate
    from app.logic.services.auth_service import argon2, login_manager
    from app.http.router import cors, router

    db.init_app(app)
    migrate.init_app(app, db)
    argon2.init_app(app)
    login_manager.init_app(app)
    cors.init_app(app)

    app.app_context().push()

    db.create_all()

    app.register_blueprint(router)

    return app


if __name__ == '__main__':
    create_app()