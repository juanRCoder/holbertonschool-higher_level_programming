#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            print(chr(ord(c) - 32), end="")
        else:
            print(c, end="")
    print()
