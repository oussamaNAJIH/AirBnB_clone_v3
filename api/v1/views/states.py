#!/usr/bin/python3
"""
import app_views from api.v1.views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.state import State
from models import storage


@app_views.route("/states", methods=["GET"])
def all_states():
    list_states = []
    for state in storage.all(State).values():
        list_states.append(state.to_dict())
    return jsonify(list_states)


@app_views.route("/states/<state_id>", methods=["GET"])
def get_state(state_id):
    obj = storage.get(State, state_id)
    if obj is not None:
        return jsonify(obj.to_dict())
    else:
        abort(404)


@app_views.route("/states/<state_id>", methods=["DELETE"])
def delete_state(state_id):
    obj = storage.get(State, state_id)
    if obj is not None:
        storage.delete(obj)
        storage.save()
    else:
        abort(404)
    return jsonify({}), 200


@app_views.route("/states", methods=["POST"])
def create_state():
    data = request.get_json()

    if not isinstance(data, dict):
        return jsonify({"error": "Not a JSON"}), 400

    if "name" not in data:
        return jsonify({"error": "Missing name"}), 400

    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=["PUT"])
def update_state(state_id):
    obj = storage.get(State, state_id)
    if not obj:
        abort(404)
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(obj, key, value)
    storage.save()

    return jsonify(obj.to_dict()), 200
