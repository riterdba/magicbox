#!/usr/bin/python3
import os
''' Работаем с модулем OS'''

''' Узнаем тип операционной системы'''
print('Ваша операционная система - ' + os.name)

print('\n')

'''Узнаем пути до системных папок'''
print('Список переменных окружения:\n')
print(os.environ)

print('\n')

'''Получаем список файлов и папок'''
print(os.listdir('/home/riterdba/testplace'))

print('\n')

'''Создаем папку'''
os.makedirs('/home/riterdba/test', exist_ok = True)

'''Удаляем файл'''
if(os.path.exists('/home/riterdba/testplace/2.py')):
    os.remove('/home/riterdba/testplace/2.py')

'''Перемещаем и переименовываем файл'''
if(os.path.exists('/home/riterdba/testplace/3.py')):
    os.replace('/home/riterdba/testplace/3.py', '/home/riterdba/test/3.py')

'''Открываем файл в системе прграммой по умолчанию'''
if(os.path.exists('/home/riterdba/testplace/zen.txt')):
    os.startfile('/home/riterdba/testplace/zen.txt')
