#!/usr/bin/python3
"""
import app_views from api.v1.views
"""
from flask import jsonify, abort
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
    else:
        abort(404)
    return jsonify({}), 200
