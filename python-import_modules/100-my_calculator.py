#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    length = len(argv) - 1

    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        operator = argv[2]
        b = int(argv[3])

        if operator == '+':
            print(f"{a} + {b} = {add(a, b)}")
        elif operator == '-':
            print(f"{a} - {b} = {sub(a, b)}")
        elif operator == '*':
            print(f"{a} * {b} = {mul(a, b)}")
        elif operator == '/':
            print(f"{a} / {b} = {div(a, b)}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
