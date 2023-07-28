#!/usr/bin/python3
"""This module has a class Rectangle that inherit from BaseGeometry
"""


class BaseGeometry:
    """" class BaseGeometry """
    def area(self):
        """function has area of figure geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validation if value is a number integer
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ class Rectangle """
    def __init__(self, width, height):
        """function init that inicialitation width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
