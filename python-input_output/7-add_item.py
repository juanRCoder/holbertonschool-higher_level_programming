#!/usr/bin/python3
"""
"""

import sys
import os.path


save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file


new_list = []
if os.path.exists("add_item.json"):
    new_list = load_file("add_item.json")

for arg in sys.argv[1:]:
    new_list.append(arg)

save_file(new_list, "add_item.json")
