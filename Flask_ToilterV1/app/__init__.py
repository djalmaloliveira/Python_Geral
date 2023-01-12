#https://www.youtube.com/watch?v=tJZjniFdaIw

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrte import Migrate, MigrateCommand


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)
migrete = Migrate(app,db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.controllers import default


