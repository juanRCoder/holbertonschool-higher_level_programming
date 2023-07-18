#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerador = sum(score * weight for score, weight in my_list)
    denominador = sum(weight for _, weight in my_list)
    result = numerador / denominador
    return result
