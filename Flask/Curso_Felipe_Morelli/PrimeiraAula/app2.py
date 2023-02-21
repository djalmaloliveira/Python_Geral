
from flask import Flask, render_template

#import flask from Flask

app = Flask(__name__)


app.run()
@app.route("/")
def homepage():
    return "Ola mundo"

if __name__== "__main__":
    app.run()