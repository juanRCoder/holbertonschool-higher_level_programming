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
        self.__size = size
        self.__position = position

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
    def position():
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
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Method that prints a # square
        """
        if self.__size == 0:
            print()
        else:
            for pst1 in range(self.__position[1]):
                print()
                for columns in range(self.__size):
                    for pst0 in range(self.__position[0]):
                        print(" ", end="")
                    for rows in range(self.__size):
                        print("#", end="")
                    print()