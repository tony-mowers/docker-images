from flask import Flask
from simple.calc import do_add

app = Flask(__name__)


@app.route('/')
def hello_world():
    result: int = do_add(5, 27)
    return f'Hello, my favorite number is {result}!'

