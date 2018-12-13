#!/usr/bin/python3
y = 64
x = 3
f = y
while True:
    z = (f + 1) % x
    if z == 1:
        break
    else:
        f += (f + 1)
print(y)
print(f)
