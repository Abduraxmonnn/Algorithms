class Solution(object):
    def climbStairs(self, n):
        ...
        # -> 1
        # Time Comp: O(N)
        if n < 3:
            return n

        st1, st2 = 1, 2
        for _ in range(n - 2):
            st1, st2 = st2, st2 + st1
        return st2

        # # -> 2
        # if n < 3:
        #     return n
        #
        # sts = [1, 2]
        # for i in range(2, n):
        #     sts.append(sts[i-2] + sts[i-1])
        # return sts[-1]

    # # -> 3
    # step = {1: 1, 2: 2}
    # def climbStairs(self, n: int) -> int:
    #     if n in self.step:
    #         return self.step[n]
    #     self.step[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
    #     return self.step[n]

if __name__ == '__main__':
    n = 6
    print(Solution().climbStairs(n))

#
#
# https://leetcode.com/problems/climbing-stairs/

# Explanation 1: https://www.youtube.com/watch?v=u43aQ4Vgvs0
# Explanation 2: https://www.youtube.com/shorts/UY6d4cv-0RI