#!/usr/bin/python3
"""
python file
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__)

# Import views at the end to avoid circular imports
from api.v1.views.index import *
from api.v1.views.states import *