import flask
from flask import request, jsonify
from location import location

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    try:
        return jsonify(location())
    except KeyError:
        return 'Failed'
