#!/usr/bin/python

from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello!"

if __name__ == '__main__':
    app.run(debug=True)