from flask import Flask
import sqlite3
import os

app = Flask(__name__)


def get_database_connection():
    database_path = os.path.join(os.getcwd(), 'databas.db')
    return sqlite3.connect(database_path)

def get_all_movies(sort_by=None):
    conn = get_database_connection()
    cursor = conn.cursor()

    # ger olika select statements beroende på sortering
    if sort_by == 'title':
        cursor.execute('SELECT image_url, title, release_year  FROM Filmer ORDER BY title')
    elif sort_by == 'release_year':
        cursor.execute('SELECT image_url, title, release_year FROM Filmer ORDER BY release_year')
    elif sort_by == 'rating':
        cursor.execute('SELECT image_url, title, release_year FROM Filmer')
    else:
        cursor.execute('SELECT image_url, title, release_year FROM Filmer')

    # delar up bilder och text i olika delar
    movies = []
    for row in cursor.fetchall():
        movies.append({
            "image_url": row[0],
            "title": row[1],
            "release_year": row[2]
        })
    conn.close()
    return movies


def get_all_directors():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT image_url ,Namn FROM Regissorer')
    data = []
    for row in cursor.fetchall():
        data.append({
            "image_url": row[0],
            "Namn": row[1],
        })
    conn.close()
    return data
    


