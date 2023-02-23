
# Flask-SQLAlchemy
# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/

from app import app

@app.route('/')
def index():
    return "Hello, World! - 9"

    
