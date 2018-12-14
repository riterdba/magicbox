#!/usr/bin/python3
'''Программа для дешифровки текстов, зашифрованных афинным шифром.'''
def decoder():
    alf = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
    x = int(input('Введите первый ключ:'))#НОД(x,y) = 1
    v = int(input('Введите второй ключ:'))
    y = int(input('Введите кодировку:'))#Кодировка русского алфавита 64
    text_cod = []
    final_cod = []
    final_text_cod = []
    if y % x != 0:
        text = input('Введите текст сообщения:')
        for i in text:
            try:
                s = alf.index(i)
                text_cod.append(s)
            except ValueError:
                continue
    else:
        print('Ключ неверен.')
    for i in range(1, y + 1):
        f = x * i
        m = f % y
        if m == 1:
            break
    f = f / x
    f = int(f)
    print(f)
    for j in text_cod:
        codd = (f * (j - v)) % y
        final_cod.append(codd)
    print(final_cod)
    for z in final_cod:
        q = alf[z]
        final_text_cod.append(q)
    final_text = ''.join(final_text_cod)
    return print(final_text)


decoder()
