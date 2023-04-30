class Solution(object):
    def isPerfectSquare(self, num):
        for i in range(1, 2**16):
            if i**2 == num:
                return True
            elif i**2 > num:
                return False


if __name__ == '__main__':
    num = 14
    print(Solution().isPerfectSquare(num))


#
#
# https://leetcode.com/problems/valid-perfect-square/submissions/
