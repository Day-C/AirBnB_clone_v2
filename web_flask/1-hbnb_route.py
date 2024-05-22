#!/usr/bin/python3
'''Start a flask application with multiple routes.'''
from flask import Flask


app = Flask(__name__)
app.config['STATIC_SLASHES'] = False


@app.route('/')
def hello():
    '''Display greeting.'''

    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    '''Display a nmae'''

    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
