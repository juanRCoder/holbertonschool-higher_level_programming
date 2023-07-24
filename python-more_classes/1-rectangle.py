#!/usr/bin/python3
"""This module is composed by a class that defines a Rectangle
"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Method that initializes the instance
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """method that returns the value of the width
        """
        return self.__width

    @property
    def height(self):
        """method that returns the value of the height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """method that defines the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """method that defines the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
