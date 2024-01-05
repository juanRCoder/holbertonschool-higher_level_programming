#!/usr/bin/python3
if __name__ == "__main__":
    for i in range(97, 123):
        if chr(i) != 'e' and chr(i) != 'q':
            print("{}".format(chr(i)), end="")
