#!/usr/bin/python3
"""
import app_views from api.v1.views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.state import State
from models import storage
from werkzeug.exceptions import NotFound, MethodNotAllowed, BadRequest


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
        raise NotFound()


@app_views.route("/states/<state_id>", methods=["DELETE"])
def delete_state(state_id):
    obj = storage.get(State, state_id)
    if obj is not None:
        storage.delete(obj)
        storage.save()
        return jsonify({}), 200
    else:
        raise NotFound()


@app_views.route("/states", methods=["POST"])
def create_state():
    data = request.get_json()

    if not isinstance(data, dict):
        raise BadRequest(description='Not a JSON')

    if "name" not in data:
        raise BadRequest(description='Missing name')

    new_state = State(**data)
    storage.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=["PUT"])
def update_state(state_id):
    obj = storage.get(State, state_id)
    if not obj:
        raise NotFound()
    data = request.get_json()
    if not isinstance(data, dict):
        raise BadRequest(description='Not a JSON')
    for key, value in data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(obj, key, value)
    storage.save()

    return jsonify(obj.to_dict()), 200
