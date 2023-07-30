#!/usr/bin/python3
"""this module has a function
"""


def class_to_json(obj):
    """ function class_to_json """
    if hasattr(obj, '__dict__'):
        obj_dict = obj.__dict__.copy()
        json_dict = {}

        for at_key, at_vl in obj_dict.items():
            if isinstance(at_vl, (list, dict, str, int, bool)):
                json_dict[at_key] = at_vl
        return json_dict
