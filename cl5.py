#!/usr/bin/python3
class Rectangle():
    def __init__(self, s1, s2):
        self.side1 = s1
        self.side2 = s2
    def calculate_perimeter(self):
        return (self.side1 + self.side2) * 2
    
class Square():
    def __init__(self, s):
        self.side = s
    def calculate_perimeter(self):
        return self.side * 4

rec1 = Rectangle(12, 34)
sq1 = Square(23)
x = [rec1, sq1]
for i in x:
    print(i.calculate_perimeter())

