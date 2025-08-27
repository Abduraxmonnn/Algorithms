class Solution:
    def isUgly(self, n):
        for j in [2, 3, 5]:
            while n % j == 0 and n != 0:
                n //= j

        return n == 1


if __name__ == '__main__':
    n = 6
    print(Solution().isUgly(n))


#
#
# https://leetcode.com/problems/ugly-number/
