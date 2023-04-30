class Solution(object):
    def missingNumber(self, nums):
        for i in range(0, len(nums)+1):
            if i not in nums:
                return i


if __name__ == '__main__':
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(Solution().missingNumber(nums))


#
#
# https://leetcode.com/problems/missing-number/
