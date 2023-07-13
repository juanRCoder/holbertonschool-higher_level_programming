#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    len_str = len(my_list) - 1
    for i in range(len_str, -1, -1):
        print("{:d}".format(my_list[i]))
