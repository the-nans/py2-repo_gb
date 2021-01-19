x = input("Введите целое число: ")
odd = 0
even = 0
for i in x:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Чётных цифр {even} нечётных {odd}")
