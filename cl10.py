#!/usr/bin/python3
class Square:
    square_list = []
    
    def __init__(self, a):
        self.a = a
        self.square_list.append(self)

sq1 = Square(1)
sq2 = Square(2)
sq3 = Square(3)
print(Square.square_list)


