#!/usr/bin/python3
"""module that contain a function"""
import json


def save_to_json_file(my_obj, filename):
    """function that save my_obj to format json in file json"""
    with open(filename, 'w', encoding="utf-8") as file:
        return json.dump(my_obj, file)
