#!/usr/bin/python3
for letter in "zyxwvutsrqponmlkjihgfedcba":
    if ord(letter) % 2 != 0:
        print("{}".format(chr(ord(letter) - 32)), end="")
    else:
        print("{}".format(letter), end="")
