#!/usr/bin/python3
"""Square module"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Init method"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Retrieve class size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set value to size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate area the Square"""
        return self.__size ** 2

    def my_print(self):
        """ Print the square"""
        if not self.size:
            print()
        else:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()
