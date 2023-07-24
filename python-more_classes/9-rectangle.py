#!/usr/bin/python3
"""This module define the class of the rectangle
"""


class Rectangle:
    """Class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Method that initializes the instance
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """Method that returns the area of a rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Method that returns the perimeter of a rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

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
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """method that defines the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """Method that return the rectangle '#'
        """
        if self.width == 0 or self.height == 0:
            return ""

        new_rectangle = ""

        for char in range(self.height):
            for char in range(self.width):
                new_rectangle += str(self.print_symbol)
            new_rectangle += '\n'

        return new_rectangle[:-1]

    def __repr__(self):
        """Method that returns the string represantion of the instance(object)
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Method that print an message
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method that returns the bigger Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Method that returns a new instance of Rectangle class
        """
        return cls(size, size)

