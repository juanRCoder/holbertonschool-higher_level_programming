#!/usr/bin/python3
"""module that contain a function"""


def write_file(filename="", text=""):
    """function that read and count length characteres"""
    with open(filename, 'w', encoding="UTF-8") as file:
        data_length = file.write(text)
    return data_length
