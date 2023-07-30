#!/usr/bin/python3
"""This module has function to json_string
"""


import json


def from_json_string(my_str):
    """ function that return from JSON to str """
    return json.loads(my_str)
