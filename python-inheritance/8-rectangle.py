#!/usr/bin/python3
"""This module has a class Rectangle that inherit from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """ class Rectangle  that inherit from BaseGeometry"""
    def __init__(self, width, height):
        """function init that inicialitation width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
