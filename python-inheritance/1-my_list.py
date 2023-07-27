#!/usr/bin/python3
class MyList(list):
    """ Class MyList """
    def print_sorted(self):
        """ Method that prints the sorted list 
        """
        lst_sorted = self[:]
        lst_sorted.sort()
        print(lst_sorted)
