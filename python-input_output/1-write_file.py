#!/usr/bin/python3
"""Document for file"""


def write_file(filename="", text=""):
    """Document for function"""
    with open(filename, 'w+') as file:
        file.write(text)
