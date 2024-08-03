#!/usr/bin/python3
""" routes for api"""
from api.v1.views import app_views
from flask import jsonify,Flask
from models import storage

@app_views.route('/status', methods=['GET'])
def status():
    """returns status"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'])
def stats():
    """returns status"""
    return jsonify(storage.count())
