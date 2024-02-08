#!/usr/bin/python3
"""Document for module"""


def inherits_from(obj, a_class):
    """Document for func"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
