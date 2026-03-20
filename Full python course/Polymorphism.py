# Two ways to achieve polymorphism: Inheritance or Duck typing

import math
from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius**2, 4)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.height*self.base*0.5

class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("Pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()}cm2")