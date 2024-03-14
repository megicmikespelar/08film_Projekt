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
    data = cursor.fetchall()
    conn.close()
    return data

def get_all_directors():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT Namn FROM Regissorer')
    data = cursor.fetchall()
    conn.close()
    return data
    


