def diagonalDifference(n, arr):
    # FIRST WAY
    res = 0

    for i in range(len(arr)):
        if i % 4 == 0:
            res += arr[i]

    for i in range(1, len(arr)-1):
        if i % 2 == 0:
            res -= arr[i]

    return abs(res)

    # # SECOND WAY
    # l_r = arr[0:len(arr):n+1]
    # r_l = arr[n-1:len(arr)-1:2]
    #
    # res = sum(l_r) - sum(r_l)
    #
    # return abs(res)


if __name__ == '__main__':
    n = 3
    # arr = [1, 2, 3, 4, 5, 6, 9, 8, 9]
    arr = [11, 2, 4, 4, 5, 6, 10, 8, -12]
    print(diagonalDifference(n, arr))


#
#
# https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
