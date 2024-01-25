#!/usr/bin/python3
"""module that contain a function"""
import json


def from_json_string(my_str):
    """function that deserialized format JSON to obj"""
    return json.loads(my_str)
