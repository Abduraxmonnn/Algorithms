class Solution(object):
    def isPowerOfTwo(self, n):
        x = 0

        if n > 1 and n % 2 == 1:
            return False

        # if n == 2 ** x:      # holasin buni uncomment qlish mumkin babi hc narsa ozgarmidi
        #     return True

        while n != 2 ** x:
            if x == 31:
                if n != 2 ** x:
                    return False

            x += 1

        return True


if __name__ == '__main__':
    n = 3
    print(Solution().isPowerOfTwo(n))


#
#
# https://leetcode.com/problems/power-of-two/
