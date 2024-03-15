from flask import Flask
import sqlite3
import os

app = Flask(__name__)


def get_database_connection():
    database_path = os.path.join(os.getcwd(), 'databas.db')
    return sqlite3.connect(database_path)

def get_all_movies():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT image_url, title, release_year FROM Filmer')
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
    cursor.execute('SELECT Namn FROM Regissorer')
    data = cursor.fetchall()
    conn.close()
    return data
    


