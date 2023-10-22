from decimal import Decimal
from math import ceil, sqrt

bb = {}
ps = {}
_n = [100, 1000, 10000]
_p = [0.001, 0.01, 0.1, 0.25, 0.5]
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


def c(n, k):
    ans_t = 1
    ans_b = 1
    if (n, k) in bb:
        return bb[(n, k)]
    elif (n, n - k) in bb:
        return bb[(n, n - k)]
    if k > n // 2:
        for i in range(k + 1, n + 1):
            ans_t *= i
        for i in range(2, n - k + 1):
            ans_b *= i
    else:
        for i in range(n - k + 1, n + 1):
            ans_t *= i
        for i in range(2, k + 1):
            ans_b *= i
    bb[(n, k)] = (ans_t, ans_b, Decimal(ans_t) / Decimal(ans_b))
    return bb[(n, k)]


def bernuli(n, p, s_n):
    c_t, c_b, c_a = c(n, s_n)
    return Decimal(Decimal(Decimal(c_a) * Decimal(Decimal(p) ** Decimal(s_n))) * Decimal(Decimal(1 - p) ** Decimal(n - s_n)))
    # return c_t * p ** s_n * (1 - p) ** (n - s_n) / c_b


for n in _n:
    for p in _p:
        # al = [bernuli(n, p, s) for s in range(n + 1)]
        print(n, p)
        mx = 0
        s_n = [i for i in range(ceil(n // 2 - sqrt(n * p * (1 - p))), int(n // 2 + sqrt(n * p * (1 - p))) + 1)]
        for s in s_n:
            print(s, bernuli(n, p, s))
            # print(s, al[s])
        gg = 0
        for s in range(6):
            gg += Decimal(bernuli(n, p, s))
            # gg += Decimal(al[s])
        print("s_n <= 5", gg)
        ind = maxes[(n, p)]
        mx = bernuli(n, p, ind)
        # mx = max(al)
        # ind = al.index(mx)
        print("max k =", ind, mx)
        print("-----------------------")

# 9.596841476810661657388913119E-122
# 9.596841476810661657388913119E-122
# max k =  5000 0.007978646139382153760440149528