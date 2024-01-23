#!/usr/bin/python3
"""module that contain class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """function that display area of the attributes"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that integer validator"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
