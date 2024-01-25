#!/usr/bin/python3
"""module that contain a function"""
import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
lista = []

if os.path.exists(filename):
    lista = load_from_json_file(filename)
else:
    lista = []

len_args = len(sys.argv) - 1
arguments = sys.argv

for i in range(len_args):
    lista.append(arguments[i + 1])

save_to_json_file(lista, filename)
