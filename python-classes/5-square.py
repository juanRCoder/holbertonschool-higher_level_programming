#!/usr/bin/python3
"""
Module 0-square
Defines a square class.
"""


class Square:
    """Class Square that defines a square.
    """
    def __init__(self, size=0):
        """Initialize method that stores the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """method area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """method to returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set the size value of the square
        """
        if not isinstance(value, int):
            raise TypeErro("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
