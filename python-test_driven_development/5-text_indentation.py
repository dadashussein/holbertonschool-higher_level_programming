#!/usr/bin/python3
"""Document for module"""


def text_indentation(text):
    """Function print text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    print("\n".join([i.strip() for i in text.split("\n")]), end="")
    print()
