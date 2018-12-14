#!/usr/bin/python3
import pyperclip
def coder_aff():
    alf = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
    x = int(input('Введите первый ключ:'))
    v = int(input('Введите второй ключ:'))
    y = int(input('Введите кодировку:'))
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
    for j in text_cod:
        codd = x * j + v
        codd = codd % y
        final_cod.append(codd)
    for z in final_cod:
            q = alf[z]
            final_text_cod.append(q)
    final_text = ''.join(final_text_cod)
    return final_text




print(coder_aff())
