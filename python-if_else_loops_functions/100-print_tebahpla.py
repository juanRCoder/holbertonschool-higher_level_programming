#!/usr/bin/python3
for l in range(122, 96, -1):
    print("{}".format(chr(l)) if l % 2 == 0 else chr(l - 32), end="")
