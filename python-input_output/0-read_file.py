#!/usr/bin/python3
"""This module has a function that print a text alone read
"""


def read_file(filename=""):
    """ function that reads a text file """
    with open(filename, "r", encoding="utf-8") as fileText:
        content = fileText.read()
        print(content, end="")
