"""
 Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
 вправо и влево на два знака.
"""
a = 5
b = 6
print(f"{a} = {bin(a)}")
print(f"{b} = {bin(b)}")

a_and_b = a & b
a_or_b = a | b
not_a = ~a
not_b = ~b
a_xor_b = a ^ b
a_twoleft = a << 2
a_tworight = a >> 2

print(f"{a} & {b} = {bin(a_and_b)}")
print(f"{a} | {b} = {bin(a_or_b)}")
print(f"~{a} = {bin(not_a)}")
print(f"~{b} = {bin(not_b)}")
print(f"{a} ^ {b} = {bin(a_xor_b)}")
print(f"{a} << 2 = {bin(a_twoleft)}")
print(f"{a} >> 2 = {bin(a_tworight)}")