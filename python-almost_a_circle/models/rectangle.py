#!/usr/bin/python3
"""Document for module"""
from models.base import Base


class Rectangle(Base):
    """Document for class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, input):
        """set value"""
        if type(input) is not int:
            raise TypeError("width must be an integer")
        if input <= 0:
            raise ValueError("width must be > 0")
        self.__width = input

    @property
    def height(self):
        """doc property"""
        return self.__height

    @height.setter
    def height(self, input):
        """doc for setter"""
        if type(input) is not int:
            raise TypeError("height must be an integer")
        if input <= 0:
            raise ValueError("height must be > 0")
        self.__height = input

    @property
    def x(self):
        """doc property"""
        return self.__x

    @x.setter
    def x(self, input):
        """doc for setter"""
        if type(input) is not int:
            raise TypeError("x must be an integer")
        if input <= 0:
            raise ValueError("x must be > 0")
        self.__x = input

    @property
    def y(self):
        """doc property"""
        return self.__y

    @y.setter
    def y(self, input):
        """doc for setter"""
        if type(input) is not int:
            raise TypeError("y must be an integer")
        if input <= 0:
            raise ValueError("y must be > 0")
        self.__y = input
