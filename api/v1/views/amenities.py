#!/usr/bin/python3
""" objects that handles all default RestFul API actions for amenities """
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('amenities', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/amenity/all_amenities.yml')
def get_amenities():
    """
    Retrieves the list of all cities objects
    of a specific State, or a specific city
    """
    list_amenities = []
    amenities = storage.all(Amenity).values()
    for amenity in amenities:
        list_amenities.append(amenity.to_dict())

    return jsonify(list_amenities)

@app_views.route('amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/amenity/get_amenity.yml', methods=['GET'])
def get_amenity(amenity_id):
    """
    Retrieves a specific city based on id
    """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict())

@app_views.route('amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/amenity/delete_amenity.yml', methods=['DELETE'])
def delete_amenity(amenity_id):
    """
    Deletes a city based on id provided
    """
    amenity = storage.get(Amenity, amenity_id)

    if not amenity:
        abort(404)
    storage.delete(amenity)
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('amenities', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/amenity/post_amenity.yml', methods=['POST'])
def post_amenity():
    """
    Creates a City
    """
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)

    new_amenity = Amenity(**request.get_json())
    new_amenity.save()

    return make_response(jsonify(new_amenity.to_dict()), 201)

@app_views.route('amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/amenity/put_amenity.yml', methods=['PUT'])
def put_amenity(amenity_id):
    """
    Updates a city based on id provided
    """
    amenity = storage.get(Amenity, amenity_id)

    if not amenity:
        abort(404)

    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)

    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)

    storage.save()
    return make_response(jsonify(amenity.to_dict()), 200)

