#!/usr/bin/python3
class Square():
    def __init__(self, a):
        self.a = a
    
    def __repr__(self):
        return ('''{} на {} на {} на {}'''.format(self.a, self.a, self.a, self.a))
sq1 = Square(10)
sq2 = Square(23)
sq3 = Square(77)
print(sq1)
print(sq2)
print(sq3)
