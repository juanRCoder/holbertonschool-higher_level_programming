#!/usr/bin/python3
""" module that contain function"""


class MyList(list):
    """ class MyList"""

    def print_sorted(self):
        """method that return list sorted"""

        print(sorted(self))
