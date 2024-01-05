#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if i != j and i <= 7 and j <= 9:
            print("{}{}, ".format(i, j), end="")
print("89")

