#!/usr/bin/python3
class MyFamily():
    def __init__(self, f, n, y, e):
        self.family_member = f
        self.name = n
        self.year_of_birth = y
        self.eye_color = e
        print('Добавлен новый родственник')
    def __repr__(self):
        return ''' Статус: {}, Имя: {}, Год рождения: {}, Глаза:  {}'''.format(self.family_member,    self.name, self.year_of_birth, self.eye_color)
myf1 = MyFamily('Папа', 'Михаил', 1986, 'Серые')
myf2 = MyFamily('Мама', 'Людмила', 1984, 'Карие')
myf3 = MyFamily('Дочь', 'Евгения', 2015, 'Карие')
myf4 = MyFamily('Сын', 'Алексей', 2017, 'Серые')
print(myf1)
print(myf2)
print(myf3)
print(myf4)
        
