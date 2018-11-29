#!/usr/bin/python3
class Horse():
    def __init__(self, name, color, rider):
        self.name = name
        self.color = color
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name
riderr = Rider('Миша')
horsee = Horse('Гроза', 'черная', riderr)
print(horsee.rider.name)    
