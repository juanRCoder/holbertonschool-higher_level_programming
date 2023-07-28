#!/usr/bin/python3
"""This module has a BaseGeometry class
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
        return value
