#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_flask(exception):
    '''calls storage.close()'''
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    """
    handls for 404 errors
    """
    return jsonify(error='Not found'), 404


if __name__ == '__main__':
    if getenv("HBNB_API_HOST"):
        host = getenv("HBNB_API_HOST")
    else:
        host = '0.0.0.0'
    if getenv("HBNB_API_PORT"):
        port = int(getenv("HBNB_API_PORT"))
    else:
        port = 5000
    app.run(host, port, threaded=True)
