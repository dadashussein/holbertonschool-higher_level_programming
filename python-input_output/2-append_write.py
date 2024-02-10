#!/usr/bin/python3
"""Document for file"""


def append_write(filename="", text=""):
    """Document for function"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
