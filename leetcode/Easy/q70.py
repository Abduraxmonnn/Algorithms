class Solution(object):
    def climbStairs(self, n):
        step_1 = 1
        step_2 = 2
        way = 0

        if n == 1:
            return 1
        if n == 2:
            return 2

        i = 2
        while i < n:
            way = step_1 + step_2
            step_1 = step_2
            step_2 = way
            i = i + 1
        return way


if __name__ == '__main__':
    n = 6
    print(Solution().climbStairs(n))

#
#
# https://leetcode.com/problems/climbing-stairs/
