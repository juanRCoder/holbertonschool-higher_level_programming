#!/usr/bin/python3
"""This module has a function that add new text
"""


def append_write(filename="", text=""):
    """function that add new text """
    with open(filename, 'a', encoding="utf-8") as txt:
        content = txt.write(text)
    return content
