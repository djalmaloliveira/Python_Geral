from flask import Flask, render_template

#app = Flask(__name__)
app=Flask(__name__,template_folder='templates')
# route -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    # return render_template("homepage.html")
    #return "Hello World. Para Djalma3 "
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # servidor do heroku

