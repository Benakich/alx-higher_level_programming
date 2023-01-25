#!/usr/bin/python3
"""Defines the square class"""


class Square:
    """Square class, contains nothing"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            length = '#' * self.__size
            breadth = ' ' * self.__position[0]
            for i in range(self.size):
                print(breadth, length, sep="")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, posit):
        if type(posit) is not tuple or len(posit) != 2\
                or type(posit[0]) is not int or type(posit[1]) is not int\
                or posit[0] < 0 or posit[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
