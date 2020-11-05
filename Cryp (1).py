import itertools


def crypval(crypword, sub):
    s = 0
    factor = 1
    for cryl in reversed(crypword):
        s += factor * sub[cryl]
        factor *= 10
    return s


def crypSolve(eq):
    L, R = eq.lower().replace(' ', '').split('=')
    L = L.split('+')
    let = set(R)
    for crypword in L:
        for cryl in crypword:
            let.add(cryl)
    let = list(let)

    numss = range(10)
    for perm in itertools.permutations(numss, len(let)):
        sol = dict(zip(let, perm))

        if sum(crypval(crypword, sol) for crypword in L) == crypval(R, sol):
            print(' + '.join(str(crypval(crypword, sol)) for crypword in L) + " = {} (mapping: {})".format(crypval(R, sol), sol))

if __name__ == '__main__':
    print("Welcome to my cryptarithm solver")
    print("Original Equation:  TEXAS + NEVADA = ALASKA")
    print("Solved Version (this may take a few seconds): ")
    crypSolve('TEXAS+NEVADA=ALASKA')