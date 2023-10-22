from decimal import Decimal
from math import ceil, sqrt, exp, pi

facts = [0 for i in range(1001)]
maxes = {(100, 0.001): 0,
(100, 0.01): 1,
(100, 0.1): 10,
(100, 0.25): 25,
(100, 0.5): 50,
(1000, 0.001): 1,
(1000, 0.01): 10,
(1000, 0.1): 100,
(1000, 0.25): 250,
(1000, 0.5): 500,
(10000, 0.001): 10,
(10000, 0.01): 100,
(10000, 0.1): 1000,
(10000, 0.25): 2500,
(10000, 0.5): 5000}


def phi(x):
    return Decimal(1) / Decimal(sqrt(Decimal(2) * Decimal(pi))) * Decimal(exp(Decimal(-(x ** Decimal(2)) / Decimal(2))))


def fac(n):
    if facts[n] != 0:
        return facts[n]
    f = 1
    for i in range(2, n + 1):
        f *= i
    facts[n] = f
    return facts[n]


def puason(n, p, s_n):
    l = Decimal(n) * Decimal(p)
    return Decimal(Decimal(Decimal(l) ** Decimal(s_n)) / Decimal(fac(s_n))) * Decimal(exp(Decimal(-l)))


def muavr(n, p, s_n):
    n, p, s_n = Decimal(n), Decimal(p), Decimal(s_n)
    x = (Decimal(s_n) - Decimal(n * p)) / Decimal(sqrt(Decimal(Decimal(Decimal(n) * Decimal(p)) * Decimal(1 - p))))
    return Decimal(1) / Decimal(sqrt(n * p * (1 - p))) * phi(x)


_n = [100, 1000, 10000]
_p = [0.001, 0.01, 0.1, 0.25, 0.5]

for n in _n:
    for p in _p:
        print(n, p)
        mx = 0
        s_n = [i for i in range(ceil(n // 2 - sqrt(n * p * (1 - p))), int(n // 2 + sqrt(n * p * (1 - p))) + 1)]
        if p > 0.1 or s_n[-1] > 1000:
            for s in s_n:
                print(s, muavr(n, p, s))
        else:
            for s in s_n:
                print(s, puason(n, p, s))
        gg = 0
        if p > 0.1:
            for s in range(6):
                gg += Decimal(muavr(n, p, s))
        else:
            for s in range(6):
                gg += Decimal(puason(n, p, s))
        print("s_n <= 5", gg)
        ind = maxes[(n, p)]
        if p > 0.1 or ind > 1000:
            mx = muavr(n, p, ind)
        else:
            mx = puason(n, p, ind)

        print("max k =", ind, mx)
        print("-----------------------")

