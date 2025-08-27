class Solution(object):
    def isPowerOfThree(self, n):
        power = 0

        if n == 0 and n % 3 != 0:
            return False

        while n != 3 ** power:
            if power == 31:
                if n != 3 ** power:
                    return False
            power += 1

        return True


if __name__ == '__main__':
    n = 27  # 617673396283947
    print(Solution().isPowerOfThree(n))

#
#
# https://leetcode.com/problems/power-of-three/


# while (n % 3 == 0 and n > 0):
#     n = n / 3
# return n == 1
