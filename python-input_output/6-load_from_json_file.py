#!/usr/bin/python3
"""module that contain a function"""
import json


def load_from_json_file(filename):
    """function that deserialized file.json"""
    with open(filename, 'r') as file:
        return json.load(file)
