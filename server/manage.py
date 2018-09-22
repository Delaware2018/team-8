import os
from flask_script import Manager
from app import db, create_app
from app import models
from flask_migrate import Migrate, MigrateCommand

app = create_app(config_name= "development")
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
