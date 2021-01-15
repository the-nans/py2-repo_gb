"""
Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f'
включительно.
"""
from random import uniform, randint
a = input("Введите нижнюю границу случайности")
b = input("Введите верхнюю границу случайности")
c = ''
if a.isdigit() and b.isdigit():
    c = randint(int(a), int(b))
else:
    if a.replace(".", "").isdigit() and b.replace(".", "").isdigit():
        c = uniform(float(a), float(b))
    else:
        if len(a) == 1 and len(b) ==1 and 96 < ord(a) < 123 and 96 < ord(b) < 123:
            lim_upper = ord(a)
            lim_lower = ord(b)
            c = chr(randint(lim_upper, lim_lower))
        else:
            print("Границы случайности не опознаны")
print(c)
