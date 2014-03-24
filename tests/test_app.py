import requests

from nose.tools import eq_
from hello import app
from multiprocessing import Process

proc = None

def setup():
    app.DATABASE = ':memory:'
    global proc
    proc = Process(target=app.app.run)
    proc.start()

def teardown():
    proc.terminate()

        
class TestApp(object):

    def test_index(self):
        r = requests.get("http://localhost:5000")
        eq_(r.content, 'http://localhost:5000/users')

    def test_users(self):
        r = requests.get("http://localhost:5000/users")
        eq_(r.content, '''[
  {
    "age": 23, 
    "link": "http://localhost:5000/users/1", 
    "id": 1, 
    "name": "buck"
  }, 
  {
    "age": 33, 
    "link": "http://localhost:5000/users/2", 
    "id": 2, 
    "name": "liz"
  }, 
  {
    "age": 48, 
    "link": "http://localhost:5000/users/3", 
    "id": 3, 
    "name": "fritz"
  }
]''')
        
    def test_user(self):
        r = requests.get("http://localhost:5000/users/1")
        eq_(r.content, '''{
  "age": 23, 
  "link": "http://localhost:5000/users/1", 
  "id": 1, 
  "name": "buck"
}''')
        
