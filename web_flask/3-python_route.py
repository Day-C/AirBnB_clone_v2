#!/usr/bin/python3
'''flask application with multiple routes.'''
from flask import Flask


app = Flask(__name__)
app.config['STATIC_SLASHES'] = False


@app.route('/')
def hello():
    '''Display greeting.'''

    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    '''Display a name'''

    return 'HBNB'

@app.route('/c/<text>')
def name(text):
    '''Display a string.'''

    text = text.replace('_', ' ')
    return f'C {text}'

@app.route('/python/<test>')
def pyth(text):
    '''Display a string.'''

    return f'Python {text}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
