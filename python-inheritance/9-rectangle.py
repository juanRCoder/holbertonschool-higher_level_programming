#!/usr/bin/python3
"""module that contain class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """check if width and heigth is integer validator"""
        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = height
    
    def __str__(self):
        return f"[Rectangle] {self._width}/{self._height}"
    
    def area(self):
        return self._width * self._height