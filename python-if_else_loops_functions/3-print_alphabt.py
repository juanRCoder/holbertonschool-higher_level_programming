#!/usr/bin/python3
alphabet = "{}"
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter != 'e' and letter != 'q':
        print(alphabet.format(letter), end="")
