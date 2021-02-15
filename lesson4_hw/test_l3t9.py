from random import randint
arr_spread = 100
arr_size = 10
def two_minimums(spread, size):
    k = []
    arr = [randint(1, arr_spread) for _ in range(arr_size)]
    for _ in range(2):
        m1 = arr_spread
        for i in arr:
            m1 = i if m1 > i else m1
        k.append(arr.pop(arr.index(m1)))
    return k


# test_l3t9.two_minimums(5,10)"
# 1000 loops, best of 5: 7.48 usec per loop

# test_l3t9.two_minimums(5,100)"
# 1000 loops, best of 5: 7.49 usec per loop

#  python3 -m timeit -n 1000 -s "import test_l3t9" "test_l3t9.two_minimums(5,1000)"
# 1000 loops, best of 5: 7.51 usec per loop

#  python3 -m timeit -n 1000 -s "import test_l3t9" "test_l3t9.two_minimums(5,1000000)"
# 1000 loops, best of 5: 7.4 usec per loop
