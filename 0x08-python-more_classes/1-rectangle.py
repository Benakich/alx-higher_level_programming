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
