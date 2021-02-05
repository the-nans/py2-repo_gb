# def dividers(p):
#     res = []
#     for i in range(1, p//2+1):
#         if p % i == 0:
#             res.append(i)
#     return res
#
# def integer_right_triangles(p):
#     res = []
#     for i in range(4, p//2+1, 4):
#         for j in range(3, p//2+1, 3):
#             if i**2 + j**2 == (p - (i + j))**2 :
#                 res.append([i, j,  p-i-j])
#     return [sorted(i) for i in res]
#
# # print(integer_right_triangles(120))
# #
# # print(dividers(1000000))
# # print(len(dividers(1000000)))
#
#
#
# for i in dividers(1000000):
#     q = integer_right_triangles(i)
#     if q != [] :
#         print(f'{i} {q}')
import cProfile

def generate(triple):
        a, b, c = triple[0], triple[1], triple[2]
        t1 = [a - 2 * b + 2 * c, 2 * a - b + 2 * c, 2 * a - 2 * b + 3 * c]
        t2 = [a + 2 * b + 2 * c, 2 * a + b + 2 * c, 2 * a + 2 * b + 3 * c]
        t3 = [-a + 2 * b + 2 * c, -2 * a + b + 2 * c, -2 * a + 2 * b + 3 * c]
        return sorted([t1, t2, t3])


def integer_right_triangles(p):
    res = []
    depth = 0
    tree = {(3, 4, 5): [], }
    if p % sum([3, 4, 5]) == 0:
        res.append([x * p // sum([3, 4, 5]) for x in [3, 4, 5]])
    while depth < 40:
        for k, v in tree.items():
            if not v:
                v.extend(generate(k))  # [], [], []
                a, b, c = tuple(generate(k)[0]), tuple(generate(k)[1]), tuple(generate(k)[2])
                tree[a], tree[b], tree[c] = [], [], []
                for i in [a,b,c]:
                    c=1
                    if p % sum(i) == 0:
                        res.append(sorted([x*p//sum(i) for x in i]))
                break
        depth += 1
    return sorted(res, key=lambda x: x[0])

#cProfile.run('integer_right_triangles(1000000)')
print(integer_right_triangles(1248))

# def walk(depth, p):
#     start = [3,4,5]
#     if depth == 1:
#         return start
#     else:
#         return generate(walk(depth-1, p))[1]
#
# print(walk(3, 408 ))