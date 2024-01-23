#!/usr/bin/python3
"""module that contain class BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """check if size is integer validator"""
        self.integer_validator("size", size)
        self._size = size
        super().__init__(self._size, self._size)

    def area(self):
        """method for display area of the square"""
        return super().area()
