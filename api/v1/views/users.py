#!/usr/bin/python3
"""
Module for user views
"""
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'])
def get_users():
    """Retrieves the list of all User objects"""
    users = [user.to_dict() for user in storage.all(User).values()]
    return jsonify(users)
