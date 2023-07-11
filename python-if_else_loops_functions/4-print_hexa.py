#!/usr/bin/python3
# :x / imprime numeros en hexa minusculas en un string format
string = "{} = 0x{:x}"
for number in range(99):
    print(string.format(number, number))
