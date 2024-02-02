#!/usr/bin/python3
"""
Module for State views
"""

from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import City


@app_views.route('/cities', methods=['GET'], strict_slashes=False)
def get_cities():
    """Retrieves the list of all city objects"""
    states = [state.to_dict() for state in storage.all(City).values()]
    return jsonify(states)


@app_views.route('/cities/<state_id>', methods=['GET'], strict_slashes=False)
def get_city(state_id):
    """Retrieves a city object"""
    state = storage.get(City, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_city(city_id):
    """Deletes a city object"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({})


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a State object"""
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400
    if 'name' not in data:
        return jsonify({"error": "Missing name"}), 400
    new_state = City(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_state(city_id):
    """Updates a City object"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400

    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(city, key, value)

    storage.save()
    return jsonify(city.to_dict())
