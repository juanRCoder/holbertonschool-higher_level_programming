#!/usr/bin/python3
numbers = "{:02d}, " # 0:2d / imprime numeros con 2 digitos.
for number in range(100):
    if number != 99:
        print(numbers.format(number), end="")
    else:
        print("{:02d}".format(number))
