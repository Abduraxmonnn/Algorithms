class Solution(object):
    def isHappy(self, n):
        d = set()

        while n == 1:
            if n in d:
                return False
            d.add(n)
            n = sum([int(i) * int(i) for i in str(n)])

        return True


if __name__ == '__main__':
    n = 12
    print(Solution().isHappy(n))


#
#
# https://leetcode.com/problems/happy-number/

# Agar chumasin debug qlb cunvolwin mumkin yoki commentni run ili oqib cunvolwin mumkn.

# shu narsa n != 1 --> n == 1 boguncha silk aylanuradi

# for i in str(n):
#     # print(int(i))
#     # print(int(i) * int(i))
#     n = sum([int(i) * int(i)])
#     print(">", n)
