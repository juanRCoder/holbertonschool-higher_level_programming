#!/usr/bin/python3
""" method that contain an class"""

class MyInt(int):
    def __init__(self, num):
        """attributes of the class"""
        self._num = num
    
    def __eq__(self, other):
        """method rebeld if attribute is not equal"""
        return self._num != other
    
    def __ne__(self, other):
        """method rebeld if attribute is equal"""
        return self._num == other