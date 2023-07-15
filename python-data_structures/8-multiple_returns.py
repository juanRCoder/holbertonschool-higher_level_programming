#!/usr/bin/python3
def multiple_returns(sentence):
    len_tuple = len(sentence)
    first_character = sentence[0]
    if not len_tuple:
        fisrt_character = None
    return len_tuple, first_character
