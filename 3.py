#!/usr/bin/python3
# Простейшие арифметические операции.
def arithmetic(x,y,z):
    if z=='+':
        return x+y
    elif z=='-':
        return x-y
    elif z=='*':
        return x*y
    elif z=='/':
        return x/y
    else: 
        return print('Неизвестная операция')
arif=arithmetic
a=int(input('Введите первое число'))
b=int(input('Введите второе число'))
c=input('Введите оперцию')
print(arif(a,b,c))
