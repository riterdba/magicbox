#!/usr/bin/python3
myname=input('Введите логин: ')
mypass=input('Введите пароль: ')
if(((myname=='mike') and (mypass=='m1234')) or ((myname=='mila') and (mypass=='ml1234'))):
    print('Добро пожаловать ')
else:
    print('В доступе отказано ')
