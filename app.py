from location import location
import requests
from flask import Flask, jsonify
app = Flask(__name__, template_folder='.')


@app.route('/location/', methods=['GET'])
def locater():
    data = location()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
