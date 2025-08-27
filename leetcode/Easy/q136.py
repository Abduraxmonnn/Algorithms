class Solution(object):
    def singleNumber(self, nums):
        elements = set(nums)
        for element in elements:
            nums.remove(element)

        for element in elements:
            if element not in nums:
                return element


if __name__ == '__main__':
    nums = [4, 4, 4, 2]
    print(Solution().singleNumber(nums))
