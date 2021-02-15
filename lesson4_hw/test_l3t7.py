from random import randint
from cProfile import run

def minimax_matrix(cols, rows):
    arr_spread = 100
    matrix = [[randint(1, arr_spread) for i in range(rows)] for k in range(cols)]
    # for line in matrix:
    #     for item in line:
    #         print(f"{item:<4}", end='')
    #     print()
    max_ = 0
    for i in range(cols):
        min_ = matrix[0][i]
        for j in range(rows):
            if matrix[j][i] < min_:
                min_ = matrix[j][i]
        if max_ < min_:
            max_ = min_
    return(max_)



#  minimax_matrix(5,5)
# 1000 loops, best of 5: 19.3 usec per loop

#  minimax_matrix(20,20)
# 1000 loops, best of 5: 258 usec per loop

#  minimax_matrix(50,50)
# 1000 loops, best of 5: 1.57 msec per loop



"""
run('minimax_matrix(20,20)')

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
      400    0.000    0.000    0.000    0.000 random.py:200(randrange)
      400    0.000    0.000    0.001    0.000 random.py:244(randint)
      400    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.001    0.001 timeit_check.py:4(minimax_matrix)
        1    0.000    0.000    0.001    0.001 timeit_check.py:8(<listcomp>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
      400    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      492    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

