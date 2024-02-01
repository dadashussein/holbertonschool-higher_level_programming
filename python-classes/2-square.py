#!/usr/bin/python3
""" Document square """


class Square:
    """Document for class"""
    def __init__(self, size=0):
        """Document init method"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
