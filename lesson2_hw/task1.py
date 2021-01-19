"""
Задача 1
Написать программу, которая будет складывать, вычитать, умножать или
делить два числа. Числа и знак операции вводятся пользователем. После
выполнения вычисления программа не завершается, а запрашивает новые
данные для вычислений. Завершение программы должно выполняться при вводе
символа '0' в качестве знака операции. Если пользователь вводит
неверный знак (не '0', '+', '-', '', '/'), программа должна
сообщать об ошибке и снова запрашивать знак операции. Также она должна
сообщать пользователю о невозможности деления на ноль, если он ввел его в
качестве делителя.
"""

x = float(input("Введите операнд 1: "))
y = float(input("Введите операнд 2: "))
while True:
    operator = input("Введите оператор - +,-,* или /: ")
    if operator == '/':
        if y == 0:
            print("На ноль делить нельзя")
            break
        print(f"{x}/{y} = {x/y:0.2f}")
        break
    elif operator == "*":
        print(f"{x}*{y} = {x*y}")
        break
    elif operator == "+":
        print(f"{x}+{y} = {x+y}")
        break
    elif operator == "-":
        print(f"{x}-{y} = {x-y}")
        break
