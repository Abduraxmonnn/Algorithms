import math


class Solution:

    def numSquares(self, n: int):
        data = []
        for i in range(1, n + 1): data.append(i)
        sample = [num for num in data if math.sqrt(num) % 2 == 0 or math.sqrt(num) % 3 == 0]
        tmp = 0
        res_1 = 0
        res_2 = 0

        for i in range(len(sample)-1):
            while tmp <= n:
                if tmp != n:
                    tmp += sample[i + 1]
                    res_1 += 1
                tmp += sample[i]
                res_1 += 1
            tmp = 0
            while tmp <= n:
                tmp += sample[i]
                n -= sample[i]
                res_2 += 1

        return min(res_2, res_1)



