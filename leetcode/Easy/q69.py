class Solution(object):
    def mySqrt(self, x):
        i = 0
        answer = 0

        if x == 1:
            return 1

        if x == 0:
            return 0

        while i < x:
            if i * i <= x:
                answer = i
            else:
                answer = i - 1
                break

            i += 1

        return answer


if __name__ == '__main__':
    x = 8
    print(Solution().mySqrt(x))


#
#
# https://leetcode.com/problems/sqrtx/
