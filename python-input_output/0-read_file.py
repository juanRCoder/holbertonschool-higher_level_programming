#!/usr/bin/python3
"""module that contain a function"""


def read_file(filename=""):
    """function that read and print a text"""
    with open(filename, 'r', encoding="utf-8") as file:
        text = file.read()

    print(text, end="")
