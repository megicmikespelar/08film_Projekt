from flask import Flask, render_template
from database import *


app = Flask(__name__)

@app.route('/')
def hello():
    data = get_all_movies()
    return render_template('index.html', movies=data)

@app.route('/filmer')
def filmer():
    return 'Detta är filmsidan.'

@app.route('/skadespelare')
def skadespelare():
    return 'Detta är skådespelarsidan.'

@app.route('/directors')
def directors():
    data = get_all_directors()
    return render_template('directors.html', directors=data)

if __name__ == '__main__':
    app.run(port=8001)