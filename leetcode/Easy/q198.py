from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # -> 1
        # O(N)
        before_prev, prev = 0, 0
        for i in range(len(nums)):
            pick = nums[i] + before_prev
            notpick = prev

            curr = max(pick, notpick)
            before_prev = prev
            prev = curr

        return prev

        # # -> 2
        # # O(N)
        # # edge cases:
        # if len(nums) == 0: return 0
        # if len(nums) == 1: return nums[0]
        # if len(nums) == 2: return max(nums)
        #
        # # dynamic programming - decide each problem by its sub-problems:
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        #
        # return dp[-1]


if __name__ == '__main__':
    # nums = [1, 2, 3, 1]  # 4
    # nums = [0, 0, 2, 7, 9, 3, 1]  # 12
    nums = [0, 0, 2, 1, 1, 2]  # 4
    #      [0, 0, 2, 1, 1, 2]
    #             lr    n
    # v = 3
    # nums = [1, 3, 1, 3, 100]  # 103
    print(Solution().rob(nums))

#
#
# https://leetcode.com/problems/house-robber/solutions/?envType=problem-list-v2&envId=dynamic-programming
# yt1: https://www.youtube.com/watch?v=kIII1uT6F8Y
# yt2: https://www.youtube.com/watch?v=br-LlFfhHbQ
# ut3: https://www.youtube.com/watch?v=73r3KWiEvyk
