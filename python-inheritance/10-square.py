#!/usr/bin/python3
"""This module has a function Square that inherit from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square """
    def __init__(self, size):
        """constructor that initializes size attribute
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """area method that return area of the square
        """
        return super().area()
