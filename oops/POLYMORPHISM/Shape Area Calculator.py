
# Polymorphism Example - Shape Area Calculator

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print("Circle Area:", math.pi * self.radius * self.radius)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print("Rectangle Area:", self.length * self.width)


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        print("Triangle Area:", 0.5 * self.base * self.height)


# Function demonstrating polymorphism
def show_area(obj):
    obj.area()


# Creating objects
c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(3, 7)

# Calling same function with different objects
show_area(c)
show_area(r)
show_area(t)