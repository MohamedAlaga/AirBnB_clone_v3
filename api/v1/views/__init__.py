#!/usr/bin/python3
from flask import Blueprint
from api.v1.views.index import *
"""
this module to define the blue print
"""
app_views = Blueprint('/api/v1')
