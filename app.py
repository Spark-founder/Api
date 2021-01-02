from flask_simple_geoip import SimpleGeoIP
import flask
from flask import request, jsonify
from location import location

app = flask.Flask(__name__)

app.config.update(GEOIPIFY_API_KEY='YOUR_API_KEY')
simple_geoip = SimpleGeoIP(app)


@app.route('/', methods=['GET'])
def home():
    try:
        return jsonify(location())
    except KeyError:
        return 'Failed'


@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    geoip_data = simple_geoip.get_geoip_data()
    return jsonify(data=geoip_data)
