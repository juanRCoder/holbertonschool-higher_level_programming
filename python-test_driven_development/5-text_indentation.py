#!/usr/bin/python3
"""Module composed by a function that prints 2 new lines after ".?:" characters
"""


def text_indentation(text):
    """Function that prints 2 new lines after ".?:" characters
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text[:]

    for char in ".?:":
        list_text = text.split(char)
        text = ""
        for i in list_text:
            i = i.strip(" ")
            text = i + char if text is "" else text + "\n\n" + i + char

    print(text[:-3], end="")
