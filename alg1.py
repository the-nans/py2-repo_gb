# 1) print('Введите два числа')
# a = int(input('введите первое число: '))
# b = int(input('введите второе число: '))
# if b!=0:
#     print(a/b)
# else:
#     print('У задачи нет решения')

# 2) num = int(input('Введите трехзначное число'))
# a = num // 100;
# b = (num % 100)//10
# c = b%10
#
# print(f'sum {a+b+c}')
# print(f'mult{a*b*c}')

# 3) x = int(input('Введите целочисленное x: '))
# if x == 0:
#     y = 0
# elif x > 0:
#     y = 2*x-10
# else:
#     y = 2*abs(x) - 1
# print(f"f(x) = {y}")

# a, b, c = [int(el) for el in input("Введите три целых числа").split()]
# max_of_three = a
# if max_of_three < b:
#     max_of_three = b
# if max_of_three < c:
#     max_of_three = c
# print(f'Max value is {max_of_three}')
# if a < b:
#     if b < c:
#         print(c)
#     else:
#         print(b)
# else:
#     if a < c:
#         print(b)
#     else:
#         print(a)

amount = int(input('Введите число'))
ed_izm = input('Введите b или k для байтов и килобайтов соотв.').lower()
if ed_izm == "k":
    print(amount/1024)
else:
    if ed_izm == "b":
        print(amount*1024)
    else:
        print("Ошибка. Вводить нало k или b")
