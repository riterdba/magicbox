#!/usr/bin/python3
"""class Square():
    def __init__(self, a, b, c):
        self.side1 = a
        self.side2 = b
        self.side3 = c

    def cange_size(self):
        x = float(input('Введите число:'))
        '''y = [self.side1, self.side2, self.side3]
        z = 0
        for i in y:
            y[z] = i + x
            z += 1'''
        self.side1 = self.side1 + x
        self.side2 = self.side2 + x
        self.side3 = self.side3 + x
sq1 = Square(3, 4, 5)
sq1.cange_size()
print(sq1.side1)
print(sq1.side2)
print(sq1.side3)
""" 
class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size

a_square = Square(100)
print(a_square.s1)

a_square.change_size(200)
print(a_square.s1)         
