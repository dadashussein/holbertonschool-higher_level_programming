#!/usr/bin/python3
"""Document for module"""


class Student:
    """Document for class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Document for method"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict

    def reload_from_json(self, json):
        """Document for method"""
        if isinstance(json, dict):
            for key, value in json.items():
                setattr(self, key, value)
