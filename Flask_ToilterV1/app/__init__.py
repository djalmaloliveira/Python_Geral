#https://www.youtube.com/watch?v=r40pC9kyoj0

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world Dj5!"



if __name__=="__main__":
    app.run(debug=True)