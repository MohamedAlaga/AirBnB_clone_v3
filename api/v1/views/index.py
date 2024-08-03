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
    Amenity = storage.count("Amenity")
    City = storage.count("City")
    Place = storage.count("Place")
    Review = storage.count("Review")
    State = storage.count("State")
    User = storage.count("User")
    return jsonify({
  "amenities": Amenity, 
  "cities": City, 
  "places": Place, 
  "reviews": Review, 
  "states": State, 
  "users": User
    })
