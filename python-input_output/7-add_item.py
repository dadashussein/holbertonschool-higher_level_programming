#!/usr/bin/python3
"""Document for module"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if os.path.isfile("add_item.json"):
    arg_obj = load_from_json_file("add_item.json")
else:
    arg_obj = []


def my_script():
    for x in range(1, len(sys.argv)):
        arg_obj.append(sys.argv[x])


my_script()
save_to_json_file(arg_obj, "add_item.json")
