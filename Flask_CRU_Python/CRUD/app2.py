from flask import Flask

app2 = Flask(__name__)


@app2.route("/")
def firstApp():
    return "<h1>Minha primeira aplicação desenvolvida em python</h1>"
    
    
if __name__=="__main__":
    app2.run(debug=True)
    
    