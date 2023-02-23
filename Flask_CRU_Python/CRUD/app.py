# https://www.youtube.com/watch?v=YZqZ3LaLm0g&list=PL93XPH6f0DHqL6K4W1Ydv3fJqotiK73XN&index=60


from flask import Flask, render_template, request, url_for, redirect

from flask.ext.sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy
#from flask_mongoalchemy import MongoAlchemy

app = Flask(__name__)
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)


class Pessoa(db.Model):
    __tablename__='cliente'
    
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    telefone = db.Column(db.String)
    cpf = db.Column(db.String)
    email= db.Column(db.String)
    
    def __init__(self, nome, telefone, cpf, email):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        
db.create_all()

@app.route("/index")
def index():
    return render_template("index.html")
    

if __name__=='__main__':
    app.run(debug=True)
    
    
    
 