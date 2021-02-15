def eratosphen(n: int):
    numbers = list(range(n+1))
    numbers[1] = 0
    for i in numbers:
        if numbers[i] != 0:
            j = i*2
            while j < n:
                numbers[j] = 0
                j += i
    result = [i for i in numbers if i != 0]
    return result[-2]

print(eratosphen(12))

# python3 -m timeit -n 1000 -s "import eratosphen" "eratosphen.eratosphen(10)"
# 1000 loops, best of 5: 1.71 usec per loop

#
#  python3 -m timeit -n 1000 -s "import eratosphen" "eratosphen.eratosphen(1000)"
# 1000 loops, best of 5: 189 usec per loop

#  python3 -m timeit -n 1000 -s "import eratosphen" "eratosphen.eratosphen(10000)"
# 1000 loops, best of 5: 2.11 msec per loop

