#!/usr/bin/python3
import math
def triangle():
    a = float(input('Первая сторона:'))
    b = float(input('Вторая сторона:'))
    c = float(input('Третья сторона:'))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s
print(triangle())


