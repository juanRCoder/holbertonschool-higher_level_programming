#!/usr/bin/python3
def uppercase(str):
    for c in str:
        letter = "{}"
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            print(letter.format(chr(ord(c) - 32)), end="")
        else:
            print(c, end="")
    print()
