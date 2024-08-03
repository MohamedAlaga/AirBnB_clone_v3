#!/usr/bin/python3
""" routes for api"""
from api.v1.views import app_views
from flask import jsonify,Flask

@app_views.route('/status', methods=['GET'])
def status():
    """returns status"""
    return jsonify({"status": "OK"})
