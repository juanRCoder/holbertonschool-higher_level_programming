#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    last_element = len(my_list) - 1
    for i in range(last_element, -1, -1):
        print("{:d}".format(my_list[i]))
