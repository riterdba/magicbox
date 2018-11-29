#!/usr/bin/python3
class Shape():
    def what_am_i(self):
        print('Я фигура')

class Rectangle(Shape):
    def __init__(self, s1, s2):
        self.side1 = s1
        self.side2 = s2
    
class Square(Shape):
    def __init__(self, s):
        self.side = s

rec1 = Rectangle(20, 10)
sq1 = Square(87)
rec1.what_am_i()
sq1.what_am_i()
