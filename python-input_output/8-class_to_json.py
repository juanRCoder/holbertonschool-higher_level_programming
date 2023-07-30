#!/usr/bin/python3
"""This module has a function that return a new attr
"""


def class_to_json(obj):
    """ function tht return the dicitionary description """

    attr = {}
   if hasattr(obj, "__dict__"):
       attr = obj.__dict__.copy()
    return attr
