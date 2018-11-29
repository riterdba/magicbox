#!/usr/bin/python3
import math
'''Расчет площади элипса'''
class Elips():
    def __init__(self, a, b):
        self.big_poluos = a
        self.sma_poluos = b
    def area(self):
        return self.big_poluos * self.sma_poluos * math.pi
eli1 = Elips(30, 10)
print(eli1.area())
        
        
