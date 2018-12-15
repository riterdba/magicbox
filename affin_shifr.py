#!/usr/bin/python3

def entered():
    global x
    global y
    global text_cod
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

def cod():
    global text_cod
    global final_cod
    for j in text_cod:
        codd = x * j + v
        codd = codd % y
        final_cod.append(codd)

def decod():
    global x
    global y
    global final_cod
    for i in range(1, y + 1):
        f = x * i
        m = f % y
        if m == 1:
            break
    f = f / x
    f = int(f)
    for j in text_cod:
        codd = (f * (j - v)) % y
        final_cod.append(codd)

def exited():
    global final_cod
    global final_text_cod
    global final_text
    for z in final_cod:
        q = alf[z]
        final_text_cod.append(q)
    final_text = ''.join(final_text_cod)
    return final_text

alf = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
x = int(input('Введите первый ключ:'))
v = int(input('Введите второй ключ:'))
y = int(input('Введите кодировку:'))
coding = int(input('Введите 1 - закодировать, 2 - раскодировать.'))
text_cod = []
final_cod = []
final_text_cod = []
entered()
if coding == 1:
    cod()
elif coding == 2:
    decod()
else:
    print('Неверный ввод!')
print(exited())
