# PUOSSON

import math


def pusson(m, a):
    surat = (a ** m) * math.e ** (-a)
    maxraj = math.factorial(m)

    result = surat / maxraj
    print(result)


def binomial_coefficient(n, m):
    # n = n
    # k = m
    surat = math.factorial(n)
    maxraj = math.factorial(m) * math.factorial((n - m))
    return surat / maxraj


def binomial(m):
    n = 22
    p = 0.8
    q = 0.2
    bc = binomial_coefficient(n, m)
    pp = (p ** m)
    pq = (q ** (n - m))
    result = bc * pp * pq
    print(result)


# pusson(4, 3)
bc = binomial_coefficient(10, 6)
# binomial(14)

print(bc)
