#!/usr/bin/python3
""" objects that handles all default API actions for Place Amenity link """
from models.place import Place
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/places/<place_id>/amenities', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/place/get_place_amenities.yml', methods=['GET'])
def get_place_amenities(place_id):
    """
    Retrieves the list of all Amenity objects of a Place
    """
    place = storage.get(Place, place_id)

    if not place:
        abort(404)

    amenities = [amenity.to_dict() for amenity in place.amenities]

    return jsonify(amenities)


@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/place/post_place_amenities.yml', methods=['POST'])
def post_place_amenity(place_id, amenity_id):
    """
    Links an Amenity object to a Place
    """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if amenity in place.amenities:
        return make_response(jsonify(amenity.to_dict()), 200)
    place.amenities.append(amenity)
    storage.save()

    return make_response(jsonify(amenity.to_dict()), 201)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/place/delete_place_amenities.yml',
           methods=['DELETE'])
def delete_place_amenity(place_id, amenity_id):
    """
    Deletes a Amenity object from a Place
    """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if amenity not in place.amenities:
        abort(404)
    place.amenities.remove(amenity)
    storage.save()

    return make_response(jsonify({}), 200)
