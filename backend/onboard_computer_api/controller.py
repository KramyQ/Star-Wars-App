import os
from flask import g
import sqlite3

def connect_db():
    sql = sqlite3.connect('./'+os.getenv('SQLITE_FILE'))
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    #Check if DB is there
    if not hasattr(g, 'sqlite3'):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)

def get_universe_routes():
    planetConnections = []
    for row in get_db().execute('SELECT * FROM ROUTES'):
        planetConnections.append({'link': [row[0], row[1]], 'travelTime': row[2]})
    close_db('No error')
    return planetConnections

