#!/usr/bin/python3
"""Flask server (variable app)
"""
import sys
import os
from flask import Flask, jsonify
from models import storage
from os import getenv
from api.v1.views import app_views
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def downtear(self):
    '''Status of your API'''
    storage.close()


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
