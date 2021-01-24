x = int(input("Введите натуральное число: "))
opt1 = x*(x+1)/2
opt2 = (x+1)*(x+2)/2
i = 0
cnt = 0
while i < x+1:
    cnt += i
    i += 1
if opt1 == cnt and opt2 == cnt+i:
    print(f"Для n = {x}: {opt1} = {cnt}")
    print(f"Для n+1 = {x+1}: {opt2} = {cnt +i}")
    print(f"Доказано методом неполной индукции")
else:
    print("Утверждение неверно или код косячный")
