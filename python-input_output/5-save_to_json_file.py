#!/usr/bin/python3
"""This module has a function that write a text json
"""


import json


def save_to_json_file(my_obj, filename):
    """ function that save to json file """
    with open(filename, 'w', encoding="utf-8") as txt:
        file_json = json.dumps(my_obj)
        content = txt.write(file_json)

