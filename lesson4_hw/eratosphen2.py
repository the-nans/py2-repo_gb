from cProfile import run


def check_sieve(num: int):
    for i in range(2, num+1):
        if num % i == 0 and i != 1 and i != num:
            return False
    return True

def non_eratosphen(n: int):
    i = 0
    j = 1
    while i < n:
        j += 1
        if check_sieve(j):
            i += 1
    return j

# python3 -m timeit -n 1000 -s "import eratosphen2" "eratosphen2.non_eratosphen(10)"
# 1000 loops, best of 5: 12 usec per loop

# python3 -m timeit -n 1000 -s "import eratosphen2" "eratosphen2.non_eratosphen(100)"
# 1000 loops, best of 5: 986 usec per loop

#  python3 -m timeit -n 1000 -s "import eratosphen2" "eratosphen2.non_eratosphen(200)"
# 1000 loops, best of 5: 4.71 msec per loop


"""
    run('non_eratosphen(100)')
     540    0.001    0.000    0.001    0.000 eratosphen2.py:8(check_sieve)
"""
