class Solution(object):
    def majorityElement(self, nums):
        sum = {}

        for i in nums:
            if i not in sum:
                sum[i] = 1
            else:
                sum[i] += 1

            if sum[i] > len(nums) / 2:
                return i


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2, 1, 1]
    print(Solution().majorityElement(nums))


#
#
# https://leetcode.com/problems/majority-element/

# https://youtu.be/eqX3WZGpma4
