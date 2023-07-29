#!/usr/bin/python3
"""This module has function 'add_attribute'
"""


def add_attribute(obj, attr_name, attr_value):
    """ function that add a new attribute or no
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
