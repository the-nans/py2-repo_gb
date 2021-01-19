from random import randint
num = randint(0, 100)
tries = 10
while True:
    if tries > 0:
        guess = int(input(f"Попытка номер {tries}. Введите число: "))
        tries -= 1
        if guess == num:
            print("Вы угадали!")
            break
        elif guess > num:
            print(f"Моё число меньше. Попыток: {tries}")
        else:
            print(f"Моё число больше. Попыток: {tries}")
    else:
        print(f"Попытки кончились. Число было {num}")
        break