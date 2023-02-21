from flask import Flask
#FLASK_ENV=development flask run

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Helo, World </h1>'


