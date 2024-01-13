#!/usr/bin/python3
""" Module that contain class Node"""


class Node:
    """ class Node """
    def __init__(self, data, next_node=None):
        """ constructor, instance parameters of the class"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """return value of the data"""
        return self.__data

    @property
    def next_node(self):
        """return value of the next_node"""
        return self.next_node

    @data.setter
    def data(self, value):
        """return new value in data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.data = value
    
    @next_node.setter
    def next_node(self, value):
        """return new value in next_node"""
        if value is not None or value is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.next_node = value
    
class SinglyLindedList:
    """class singlyLindedList"""

    def __init__(self, head):
        """ constructor, instance parameters of the class"""
        self.head = head

    def sorted_insert(self, value):
        """ sorted list of the numbers"""
        sorted(value)
    
    print(sorted_insert)