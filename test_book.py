#!/usr/bin/python3
import pyperclip
import re
import math

def chastot():
    text = pyperclip.paste()
    text = text.replace(' ', '')
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('!', '')
    text = text.replace(':', '')
    text = text.replace('?', '')
    text = text.replace(';', '')
    text = text.replace('"', '')
    text = text.lower()
    alf = 'абвгдежзийклмнопрстуфхцчшщъыьэюя '
    y = len(text)
    print(y)
    for i in alf:
        x = re.findall(i, text)
        x = len(x)
        z = (100 / float(y)) * x
        z = "%.2f" % z

        print('Буква:____{}____{}____{} %'.format(i, x, z))

chastot()
