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
    
    @property
    def position(self):
        return self.__position
    
    @size.setter
    def size(self, value):
        """Document for setter property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    @position.setter
    def position(self, value):
        """Document for setter property"""
        if not (
                isinstance(value, tuple)
                and len(value) == 2
                and all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Document for method"""
        return self.__size ** 2

    def my_print(self):
        """ Print the square"""
        if not self.size:
            print()
        else:
            for row in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for column in range(self.__position[0]):
                    print(" ", end="")
                for column in range(self.__size):
                    print("#", end="")
                print()
