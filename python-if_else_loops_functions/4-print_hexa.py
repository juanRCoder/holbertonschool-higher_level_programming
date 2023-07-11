#!/usr/bin/python3
string = "{} = 0x{:x}"
for number in range(98):
    print(string.format(number, number))
