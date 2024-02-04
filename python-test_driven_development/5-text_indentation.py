#!/usr/bin/python3
"""Document for module"""


def text_indentation(text):
    """Function print text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = ""
    for char in text:
        if char in ".?:":
            new_text += "\n\n"
        else:
            new_text += char
    print(new_text.strip(), end="")
    return new_text.strip()
