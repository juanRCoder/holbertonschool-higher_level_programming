#!/usr/bin/python3
"""
Module 0-square
Defines a square class.
"""


class Square:
    """Class Square that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize method that stores the size of the square
        """
        self.size = size
        self.position = position

    def area(self):
        """method area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """method to returns the size value
        """
        return self.__size

    @property
    def position(self):
        """method to returns the position value
        """
        return self.__position

    @size.setter
    def size(self, value):
        """Method to set the size value of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """method to set the positions of a square
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Method that prints a # square
        """
        if self.__size == 0:
            print()
        else:
            for ejeY in range(self.__position[1]):
                print()
            for columns in range(self.__size):
                for ejeX in range(self.__position[0]):
                    print(" ", end="")
                for rows in range(self.__size):
                    print("#", end="")
                print()
