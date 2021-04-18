from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app
from app.database.models.database_init import db
from app.database.models.main_models import init_models

manager = Manager(create_app)
migrate = Migrate(create_app, db=db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    init_models()
    manager.run()
