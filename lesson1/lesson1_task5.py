"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""
import string
a = int(input("Введите код символа в таблице ASCII: "))
if 96 < a < 123 or 64 < a < 91:
    print(chr(a))
else:
    print("Это не буква, извините")

string.ascii_letters