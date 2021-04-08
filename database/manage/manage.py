from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app
from database.models.database_init import db
from database.models.main_models import init_models

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    init_models()
    manager.run()
