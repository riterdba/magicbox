#!/usr/bin/python3
x = float(input('Введите число:'))
y = [3, 4, 5]
z = 0
for i in y:
    y[z] = i + x
    z += 1
print(y)
