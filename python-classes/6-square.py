#!/usr/bin/python3
"""Document for module"""


class Square:
    """Document for class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Document for size method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Document for setter property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Document for method"""
        return self.size ** 2

    def my_print(self):
        """Document for method"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print("{}{}".format(" " * self.position[0], "#" * self.size))
