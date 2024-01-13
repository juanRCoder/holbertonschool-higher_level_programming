#!/usr/bin/python3
"""This module contain class square"""


class Square:
    """ class square"""
    def __init__(self, size=0, position=(0, 0)):
        """ Constructor of the class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """getter for retrieve size of the square """
        return self.__size

    @property
    def position(self):
        """getter for retrieve position of the square """
        return self.__position

    @size.setter
    def size(self, value):
        """setter for change value of the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """setter for change value of the position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """method that return area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """method for print square with positions"""
        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print()
        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print("_", end="")
            for _ in range(self.__size):
                print("#", end="")
            print()
