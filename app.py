import flask
from flask import request, jsonify
import pandas as pd
from datetime import datetime as dt

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    try:
        return jsonify({
            'name': 'Dhruv'
        })
    except KeyError:
        return 'Failed'
