from sys import setrecursionlimit
setrecursionlimit(3000)


def atob(a, b):
    if a == b:
        return f"{a}"
    if a > b:
        return f"{a} , {atob(a - 1, b)}"
    if a < b:
        return f"{a}, {atob(a + 1, b)}"

# глубина рекурсси в Питоне - 1000


def akk(m, n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return akk(m-1, 1)
    return akk(m-1, akk(m, n-1))


def nod(p, q):
    m = abs(p)
    n = abs(q)
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m


def nod2(m, n):
    if n == 0:
        return m
    return nod2(n, m % n)


def nod3(n, m):
    while n != 0:
        m, n = n, m % n
    return m


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
    return result


def dectobin(n):
    i = 2
    sett = []
    while i <= n:
        sett.append(i)
        i *= 2
    presum = 0
    for j in range(len(sett)-1, -1, -1):
        if presum+sett[j] <= n:
            presum += sett[j]
            sett[j] = 1
        else:
            sett[j] = 0
    result = ""
    for j in sett:
        result = f'{j}{result}'
    return result

def likes(names):
    if len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2 or len(names)==3:
        names[-1] = f"and {names[-1]} like this"
        for i in names:
            result = f"{result}, {i}"
    elif len(names)>3:
        result = f"{names[0]}, {names[1]} and {len(names)-2} others like this"
    elif len(names) == 0:
        return "no one likes this"
    return result



def dnatranslate(dna : str, frames = [1,2,3,-1,-2,-3]):
    codons = {'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
              'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
              'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT': 'S', 'AGC': 'S', 'CCT': 'P', 'CCC': 'P',
              'CCA': 'P', 'CCG': 'P', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCT': 'A', 'GCC': 'A',
              'GCA': 'A', 'GCG': 'A', 'TAT': 'Y', 'TAC': 'Y', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
              'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
              'TGT': 'C', 'TGC': 'C', 'TGG': 'W', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R',
              'AGG': 'R', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 'TAA': '*', 'TGA': '*', 'TAG': '*'}

    def mapdna(dna_to_map):
        mapper = {'A': 'T',
                  'T': 'A',
                  'G': 'C',
                  'C': 'G'}
        result = ""
        count = 0
        while count < len(dna_to_map):
            result = f"{mapper[dna_to_map[count]]}{result}"
            count += 1
        return result
    frames_map = {1: 0, 2: 1, 3: 2, -1: 0, -2: 1, -3: 2}
    resres = []
    res = ""
    for frame in frames:
        dna_copy = dna[::] if frame > 0 else mapdna(dna)
        cnt = frames_map[frame]
        divided = ""
        while cnt < len(dna_copy):
            divided = f"{divided}{dna_copy[cnt]}"
            cnt += 1
            if (cnt - frames_map[frame]) % 3 == 0:
                res = f"{res}{codons[divided]}"
                divided = ""
        resres.append(res)
        res = ""
    return resres


# print(dnatranslate('AAA', [1]))
# print(dnatranslate('AA', [2]))
# print(dnatranslate('AAA', [-1]))
print(dnatranslate("",[]))