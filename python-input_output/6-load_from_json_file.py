#!/usr/bin/python3
"""This module has a function load from json_file
"""


import json


def load_from_json_file(filename):
    """ function that load_from_json_file """
    with open(filename, 'r', encoding="utf-8") as txt:
        js_str = json.load(txt)
        return js_str
