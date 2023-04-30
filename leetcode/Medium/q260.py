class Solution(object):
    def singleNumber(self, nums):
        elements = set(nums)
        singles = []

        for el in elements:
            nums.remove(el)

        for i in elements:
            if i not in nums:
                singles.append(i)

        return singles


if __name__ == '__main__':
    nums = [1, 2, 1, 3, 2, 5]
    print(Solution().singleNumber(nums))


#
#
# https://leetcode.com/problems/single-number-iii/
