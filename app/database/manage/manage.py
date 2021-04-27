from flask_migrate import Migrate, MigrateCommand

from app.database.models.main_models import init_models

migrate = Migrate()

if __name__ == '__main__':
    init_models()
