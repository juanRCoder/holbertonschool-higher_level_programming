#!/usr/bin/python3
"""module that contain a function"""
import json


def to_json_string(my_obj):
    """function that convert obj to format JSON"""
    return json.dumps(my_obj)
