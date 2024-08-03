#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify
"""
this module for defining the routes of the views
"""
@app_views.route('/status')
def index():
  """
  route to check the status
  """
  return jsonify({"status":"OK"})
