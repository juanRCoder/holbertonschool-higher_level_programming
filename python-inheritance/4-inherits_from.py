#!/usr/bin/python3
"""This module has a function that returns True/False
   if obj is an instance of a_class
"""


def inherits_from(obj, a_class):
    """Function that returns True/False if obj is an instance of a_class
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
