#!/usr/bin/python3
"""Document for module"""
import json


def save_to_json_file(my_obj, filename):
    """Document for function"""
    json_file = json.dumps(my_obj)
    with open(filename, "w") as file:
        file.write(json_file)
