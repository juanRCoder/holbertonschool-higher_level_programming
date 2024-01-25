#!/usr/bin/python3
"""module that contain a function"""


def append_write(filename="", text=""):
    """function that append a string at the end of a file"""
    with open(filename, 'a', encoding="UTF-8") as file:
        length_data = file.write(text)

    return length_data
