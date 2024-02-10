#!/usr/bin/python3
"""Document for file"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    with open(filename, 'r') as file:
        print(file.read(), end="")
