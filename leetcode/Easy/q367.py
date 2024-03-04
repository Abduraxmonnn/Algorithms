class Solution(object):
    def isPerfectSquare(self, num):
        i = 1
        while i * i <= num:
            if (num % i == 0) and (num / i == i):
                return True
            i = i + 1
        return False


if __name__ == '__main__':
    num = 14
    print(Solution().isPerfectSquare(num))

#
#
# https://leetcode.com/problems/valid-perfect-square/submissions/
