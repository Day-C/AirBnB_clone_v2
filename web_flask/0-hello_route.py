#!/usr/bin/python3
'''Start a flsk web applicatoin.'''
from flask import Flask


app = Flask(__name__)
app.config['STRICT_SLASHES'] = False

@app.route('/')
def hello():
    '''hello is displays greeting message'''

    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
