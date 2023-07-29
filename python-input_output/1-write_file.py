#!/usr/bin/python3
"""This module has a function that write a text
"""


def write_file(filename="", text=""):
    """ function that write a text """
    with open(filename, 'w', encoding="utf-8") as textFile:
        content = textFile.write(text)
        return content
