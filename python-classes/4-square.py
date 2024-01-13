#!/usr/bin/python3
"""This module contain class square"""


class Square:
    """ class square"""
    def __init__(self, size=0):
        """ Constructor of the class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """method that return area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """getter for retrieve size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """setter for change value of the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
