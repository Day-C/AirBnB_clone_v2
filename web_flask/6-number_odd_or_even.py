#!/usr/bin/python3
'''flask application with multiple routes.'''
from flask import Flask, render_template


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

@app.route('/number/<int:n>')
def num_route(n):
    '''Display an integer.'''

    return f'{n} is a number'

@app.route('/number_template/<int:n>')
def h1_page(n):
    '''Display html page when n is a number.'''

    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>')
def odd_or_Even(n):
    '''Renders dynamic content based on input(even of odd).'''

    n_status = ""
    if n % 2 == 0:
        n_status = "is even"
    else:
        n_status = "is odd"

    return render_template('6-number_odd_or_even.html', n=n, status=n_status)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
