#!/usr/bin/python3
def season(mes):
    if mes==12:
        return 'Зима'
    elif mes>=2:
        return 'Зима'
    elif mes<=3:
        return 'Весна'
    elif mes>=5:
        return 'Весна'
    elif mes<=6:
        return 'Лето'
    elif mes<=8:
        return 'Лето'
    elif mes>=11:
        return 'Осень'
    elif mes<=9:
        return 'Осень'
    else:
        return 'Ошибка ввода'
print(season(1233))

