#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    len_elements = len(argv) - 1
    if len_elements == 0:
        print("0 arguments.")
    elif len_elements == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments: ".format(len_elements))
        for element in range(1, len_elements + 1):
            print("{}: {}".format(element, argv[element]))
