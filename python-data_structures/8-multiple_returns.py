#!/usr/bin/python3
def multiple_returns(sentence):
    len_str = len(sentence)
    if len_str == 0:
        first_character = None
    else:
        first_character = sentence[0]
    return len_str, first_character
