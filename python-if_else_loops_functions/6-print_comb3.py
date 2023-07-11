#!/usr/bin/python3
# :d / indica numeros de 1 digito, sin ceros inciales, sin campo especifico.
numbers = "{:d}{:d}"
for num1 in range(9):
    for num2 in range(num1 + 1, 10):
        print(numbers.format(num1, num2), end="")
        if num1 != 8 or num2 != 9:
            print(", ", end="")
        else:
            print()
