#!/usr/bin/python3
y = 64
x = 9

for i in range(1, y + 1):
    w = x * i
    m = w % y
    if m == 1:
        break
w = w / x

print(w)
