#!/usr/bin/python3
"""Document for module"""
import json


def save_to_json_file(my_obj, filename):
    """Document for function"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
