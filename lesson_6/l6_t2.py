from collections import deque, defaultdict

"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, 
элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел 
из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


class HexNumber:
    def __init__(self, inputs: str,
                 v0x=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')):
        self.n1 = defaultdict(lambda: '0')
        for i, j in enumerate(reversed(inputs)):
            self.n1[i] = j
        self.v0x = v0x

    def __add__(self, other):
        v0x = self.v0x
        n1 = self.n1 if len(self.n1) > len(other.n1) else other.n1
        n2 = other.n1 if len(self.n1) > len(other.n1) else self.n1

        res = defaultdict(lambda: 0)
        for i in n1.keys():
            res[i] = v0x.index(n1[i]) + v0x.index(n2[i])
        i = 0
        while i < len(res.keys()):
            if res[i] // len(v0x) == 1:
                res[i] = res[i] % len(v0x)
                res[i + 1] += 1
            i += 1
        return HexNumber(''.join([v0x[i] for i in reversed(res.values())]), self.v0x)

    def __mul__(self, other):
        n2 = other.n1
        v0x = self.v0x
        cycle = 0
        res = HexNumber('0' * max(len(self.n1), len(other.n1)), self.v0x)
        for i, j in n2.items():
            cycle += v0x.index(j) * (len(v0x) ** i)
        for i in range(cycle):
            res = res + self
        return res

    def __str__(self):
        return ''.join(list(reversed(self.n1.values())))


nn1 = HexNumber(input('n1? '))
nn2 = HexNumber(input('n2? '))
ops = input('sum or mult? ')

if ops == 'sum':
    print(nn2 + nn1)
elif ops == 'mult':
    print(nn1 * nn2)
else:
    print('You need to enter "sum" or "mult"')
