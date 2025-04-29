list_length = len("Hello World")

print(list_length)

length = len([1 ,4, 5, 6])

print(length)

summ = sum([3, 6, 7, 2, 3, 1, 6, 4])

print(summ)

maxx = max([4 , 56, 23, 53,223, 53,2132])

print(maxx)

import math 

class shape:
    def area(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

Circle = circle(5)

print(Circle.area)