# """
# 1. Найти простые числа в диапазоне
#         2. взять простое число
#         3. сложить его цифры
#         4. вызвать функцию сложения цифр простого числа
#         5. если результат - одно число, перестать вызывать и вернуть это число
#     6. если результат единица - увеличить счётчик
# 7. вернуть счётчик
# """
# from functools import reduce
#
# def eratosphen( m:int, n: int):
#     numbers = list(range(n+1))
#     for i in numbers:
#         if numbers[i] != 0 and numbers[i] != 1:
#             j = i*2
#             while j < n:
#                 numbers[j] = 0
#                 j += i
#
#     result = [i for i in numbers if i != 0 and m <= i < n]
#     return result
#
#
#
# # def sum_num(x: int):
# #     if x // 10 == 0:
# #         return 1 if x == 1 else 0
# #     else:
# #         return sum_num(sum(list(map(lambda y: int(y)**2, list(str(x))))))
#
# def sum_num(x:int):
#     xstr = list(str(x))
#     s = ''
#     while len(xstr) > 1:
#         xstr = list(str(sum([int(i)**2 for i in xstr])))
#     return 1 if xstr == ['1'] else 0
#
#
# def solve(a,b):
#     return list(map(lambda x: sum_num(x), eratosphen(a, b))).count(1)
#
# print(solve(1, 10))

'''
create phone number
'''


def create_phone_number(n):
    n1 = ''.join([f'{x}' for x in n])
    r = f'({n1[0:3:]}) {n1[3:6:]}-{n1[7:10]}'
    return r


'''
check if prime or not
'''


def is_prime(num):
    modnum = abs(num)
    if int(f'{modnum}'[-1::]) in [0, 1, 2, 4, 6, 8] and modnum != 2:
        return False
    else:
        div = 3
        while div <= modnum ** 0.5:
            if modnum % div == 0:
                return False
            div += 2
    return True


''' 
count duplicates in string
'''
from functools import reduce


def duplicate_count(text):
    return 0 if text == '' else reduce(lambda x, y: x + y,
                                       [1 if text.upper().count(i) > 1 else 0 for i in list(set(list(text.upper())))])


'''
find all integer right triangles
'''
from functools import reduce


def integer_right_triangles(p):
    # res = []
    # for i in range(4, p//2+1, 4):
    #     for j in range(3, p//2+1, 3):
    #         if i**2 + j**2 == (p - (i + j))**2 :
    #             res.append([j, i, p-i-j])
    # return res
    res = [i ** 2 for i in range(p + 1)]
    return res


"""
fibonacci
"""
import functools

@functools.lru_cache()
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def test_fibonacci(fib):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i, res in enumerate(lst):
        assert fib(i) == res
    print('test ok')


"""
python3 -m timeit -n 1000 -s "import sandbox" "sandbox.fibonacci(10)"
55
test ok
1000 loops, best of 5: 19.6 usec per loop

python3 -m timeit -n 1000 -s "import sandbox" "sandbox.fibonacci(15)"
55
test ok
1000 loops, best of 5: 219 usec per loop

python3 -m timeit -n 1000 -s "import sandbox" "sandbox.fibonacci(20)"
55
test ok
1000 loops, best of 5: 2.49 msec per loop

"""
"""
 177/1    0.000    0.000    0.000    0.000 sandbox.py:96(fibonacci) <-- 10
 1973/1    0.000    0.000    0.000    0.000 sandbox.py:96(fibonacci)  <-- 15
 21891/1    0.005    0.000    0.005    0.005 sandbox.py:96(fibonacci)  <-- 20
  
"""
from cProfile import run


def fib_dic(n):
    _d = {0: 0, 1: 1, 2: 1}

    def _dic(n):
        if n in _d:
            return _d[n]
        else:
            _d[n] = _dic(n - 1) + _dic(n - 2)
            return _d[n]

    return _dic(n)


"""
python3 -m timeit -n 1000 -s "import sandbox" "sandbox.fib_dic(20)"
test ok
1000 loops, best of 5: 5.36 usec per loop

 python3 -m timeit -n 1000 -s "import sandbox" "sandbox.fib_dic(100)"
test ok
1000 loops, best of 5: 30.2 usec per loop
"""

"""
 run('fib_dic(100)')
 1    0.000    0.000    0.000    0.000 sandbox.py:131(fib_dic)
 197/1    0.000    0.000    0.000    0.000 sandbox.py:133(_dic)
"""


def fib_lst(n):
    _d = [None] * 1001
    _d[:2] = [0, 1]

    def _dic(n):
        if _d[n] is None:
            _d[n] = _dic(n - 1) + _dic(n - 2)
        return _d[n]

    return _dic(n)


"""
"sandbox.fib_lst(10)"
1000 loops, best of 5: 8.01 usec per loop

"sandbox.fib_lst(20)"
1000 loops, best of 5: 11.7 usec per loop

"sandbox.fib_lst(500)"
1000 loops, best of 5: 230 usec per loop

"""


def fib_loop(n):
    if n < 2:
        return n
    else:
        first, second = 0,1
        for i in range(1,n):
            first, second = second, second+first

        return second

"""
python3 -m timeit -n 1000 -s "import sandbox" "sandbox.fib_loop(100)"
1000 loops, best of 5: 3.44 usec per loop

python3 -m timeit -n 1000 -s "import sandbox" "sandbox.fib_loop(1000)"
1000 loops, best of 5: 58.4 usec per loop

python3 -m timeit -n 1000 -s "import sandbox" "sandbox.fib_loop(10000)"
1000 loops, best of 5: 1.51 msec per loop
"""

