#!/usr/bin/python3
class Dog():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
class Person():
    def __init__(self, name):
        self.name = name
viktor = Person('Виктор')
aiger  = Dog('Айгер', 'метис', viktor)
print(aiger.owner. name)
