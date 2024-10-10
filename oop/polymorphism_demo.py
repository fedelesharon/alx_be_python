# polymorphism_demo.py

import math

class Shape:
    def area(self):
        """Raise an error if not overridden in the derived class."""
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize the circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)
