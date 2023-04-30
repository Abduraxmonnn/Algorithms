def sortedSum(a):
    n = len(a)
    b = [i for i in range(1, n + 1)]
    ar = [0] * (n)
    ans = 0
    MOD = 10 ** 9 + 7
    for i in range(len(a)):
        for j in range(n - i):
            ar[j + i] += a[i] * b[j]

    for i in range(n):
        ans += ar[i]
    ans = ans % MOD
    return ans


if __name__ == '__main__':
    a = [3, 9, 5, 8]
    print(sortedSum(a))
