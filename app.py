from flask import Flask, render_template, request
from database import *


app = Flask(__name__)

@app.route('/')
def hello():
    sort_by = request.args.get('sort_by')
    data = get_all_movies(sort_by)
    return render_template('index.html', movies=data, sort_by=sort_by)


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