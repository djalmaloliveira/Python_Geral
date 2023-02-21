from flask import FLask


app = FLask(__name__)

@app.route('/')

def raiz():
    return 'Ola mundo'

app.run()


