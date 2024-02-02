#!/usr/bin/python3
"""
import app_views from api.v1.views
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

@app_views.route("/status")
def status():
    return jsonify(status='OK')

@app_views.route("/stats")
def stats():
    classes = {"amenities": Amenity, "cities": City,
           "places": Place, "reviews": Review, "states": State, "users": User}
    dict = {}
    for key, value in classes.items():
        dict[key] = storage.count(value)
    return jsonify(dict)
