#!/usr/bin/python3
def decoder():
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
    f = y
    while True:
        w = (f + 1) % x
        if w == 1:
            break
        else:
            f += (f + 1)
    f = f / 3
    f = int(f)
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
