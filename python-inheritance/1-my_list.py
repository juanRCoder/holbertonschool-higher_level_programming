#!/usr/bin/python3
"""This module MyList
"""
class Mylist(list):
    """ class Mylist"""
    def print_sorted(self):
        """Method that prints the sorted list
        """
        lst_copy = self[:]
        lst_copy.sort()
        print(lst_copy)
