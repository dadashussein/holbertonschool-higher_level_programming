#!/usr/bin/python3
"""Document for module"""
import json


def load_from_json_file(filename):
    """Document for function"""
    with open(filename, "r") as file:
        return json.load(file)
