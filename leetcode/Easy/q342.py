class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        power = 0

        if n == 0 and n % 4 != 0:
            return False

        while n != 4 ** power:
            if power == 31:
                if n != 4 ** power:
                    return False
            power += 1

        return True


if __name__ == '__main__':
    n = 16
    print(Solution().isPowerOfFour(n))

#
#
# https://leetcode.com/problems/power-of-four/submissions/920694708/
