#!/usr/bin/python3
def multiple_returns(sentence):
    len_tuple = len(sentence)
    first_character = sentence[0]
    if len_tuple <= 0:
        fisrt_character = None
    return len_tuple, first_character
