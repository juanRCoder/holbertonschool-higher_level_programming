#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    arguments = argv
    length = len(argv)
    
    if length < 2:
        print("0 argument.")
    elif length < 3:
        print("1 arguments:")
        print(f"1: {arguments[1]}")
    else:
        print(f"{length - 1} arguments:")
        for i in range(1, length):
            print(f"{i}: {arguments[i]}")
