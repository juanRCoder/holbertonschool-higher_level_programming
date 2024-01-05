#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and n <= len(str):
        temp = list(str)
        del temp[n]
        return ''.join(temp)
    else:
        return str
