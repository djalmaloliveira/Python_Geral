# https://www.youtube.com/watch?v=r40pC9kyoj0
# https://www.youtube.com/watch?v=Pz9rayiDHW0
# https://palletsprojects.com/p/flask/

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# @app.route('/')
# def index():
#     return "Hello, World! - 4"

# if __name__ == '__main__':
#     app.run(debug=True)
    
from app.controllers import default
