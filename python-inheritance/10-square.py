#!/usr/bin/python3
"""Document for module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Document for class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
