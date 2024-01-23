#!/usr/bin/python3
"""module that contain class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """class Square"""
    def __init__(self, size):
        """check if size is integer validator"""
        self.integer_validator("size", size)
        self._size = size

    def __str__(self):
        """special method for information"""
        return f"[Rectangle] {self._size}/{self._size}"

    def area(self):
        """method for display area of the square"""
        return self._size * self._size
