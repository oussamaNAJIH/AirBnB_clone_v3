#!/usr/bin/python3
"""
Module for user views
"""
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.user import User
