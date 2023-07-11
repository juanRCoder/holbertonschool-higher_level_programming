#!/usr/bin/python3
def print_last_digit(number):
    # abs / valor absoluto de un numero sin importar + o -
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
