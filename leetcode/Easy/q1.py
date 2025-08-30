class Solution(object):
    def twoSum(self, nums, target):
        # -> 1
        for i in range(len(nums)):
            a = target - nums[i]
            if a in nums and i != nums.index(a):
                return [i, nums.index(a)]

        # # -> 2
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))

# ( for a in range(i + 1, len(nums)): ) " i "dan 1ci indexdagi soni yoki holagan indexdagi soni oladi ca
# " a "da " i " digidan 1ta index oldinda yuradi. Chunki bular " range() "ning ichiga yozilvoti.
# https://leetcode.com/problems/two-sum/submissions/
