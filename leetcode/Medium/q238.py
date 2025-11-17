from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # -> 1
        # O(N)
        result = [1] * len(nums)

        prefix = 1
        for idx, num in enumerate(nums):
            result[idx] = prefix
            prefix *= num

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


if __name__ == '__main__':
    nums = [1, 2, 4, 6]
    print(Solution().productExceptSelf(nums))

#
#
# https://leetcode.com/problems/product-of-array-except-self/
