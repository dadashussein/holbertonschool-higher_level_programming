#!/usr/bin/python3
"""Document for module"""
import json


class Base:
    """Document for class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is not None or []:
            return json.dumps(list_dictionaries)
        else:
            return []
