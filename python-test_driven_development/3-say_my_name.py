#!/usr/bin/python3
"""This module is composed by a function prints a message
"""


def say_my_name(first_name, last_name=""):
    """This function prints the first and last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        return print("My name is {} {}".format(first_name, last_name))
    else:
        return print("My name is {}".format(first_name))
