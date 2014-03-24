import json
import sqlite3
from flask import Flask, g

DATABASE = '/tmp/hello.db'
CREATE_QUERY = 'CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)'
INSERT_QUERY = 'INSERT INTO users (name, age) VALUES (?, ?)'
USERS_QUERY = 'SELECT * FROM users'
USER_QUERY = 'SELECT * FROM users where id = ?'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        cur = db.cursor()
        cur.execute(CREATE_QUERY)
        for name, age in (('buck', 23), ('liz', 33), ('fritz', 48)):
            cur.execute(INSERT_QUERY, [name, age])
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def get_user(user):
    return {
        'id': user[0],
        'age': user[1],
        'name': user[2],
        'link': 'http://localhost:5000/users/{0}'.format(user[0])
    }


@app.route('/')
def index():
    return 'http://localhost:5000/users'


@app.route('/users')
def users():
    cur = get_db().cursor()
    users = [get_user(user) for user in cur.execute(USERS_QUERY)]
    return json.dumps(users)


@app.route('/users/<user_id>')
def user(user_id):
    cur = get_db().cursor()
    cur.execute(USER_QUERY, user_id)
    user = get_user(cur.fetchone())
    return json.dumps(user)

if __name__ == '__main__':
    app.run(debug=True)
