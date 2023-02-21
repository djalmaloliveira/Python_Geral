#D:\Work\Livro

from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    nome = 'Alisson'
    posts = ['Flask Basico','Flask Intermediario','Flask Avancado']
    return render_template("index.html")
    #return 'Novo mundo4'


#def index():
#	return '<h1>Hello World5!</h1>'


if __name__ == '__main__':
	app.run(debug=True)