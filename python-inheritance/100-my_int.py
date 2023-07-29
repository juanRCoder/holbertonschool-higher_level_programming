#!/usr/bin/python3
"""this module has a class MyInt rebel
"""


class MyInt(int):
    """ class Myint "rebel" that inherit from int """
    def __eq__(self, number):
        """equivalent method that return no equivalent method '!='
        """
        return super().__ne__(number)

    def __ne__(self, number):
        """no equivalent method that return equivalent method '=='
        """
        return super().__eq__(number)
