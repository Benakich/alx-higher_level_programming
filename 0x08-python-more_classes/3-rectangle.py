#!/usr/bin/python3
"""Defining a Rectangle class"""


class Rectangle:
    """Defining the Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialising a rectangle class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Defining width property"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """def height property"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def __str__(self):
        """Return rectangle string"""
        if self.width == 0 or self.height == 0:
            return ""
        string = ""
        for y in range(self.height - 1):
            string += '#' * self.width + '\n'
        string += '#' * self.width
        return string

    def area(self):
        """Return area of a rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Return perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)
