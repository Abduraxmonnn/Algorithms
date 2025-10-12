class Solution(object):
    def twoSum(self, nums, target):
        # # -> 1
        # # O(N^2)
        # for i, j in enumerate(nums):
        #     tmp = target - j
        #     for idx in (range(i + 1, len(nums))):
        #         if tmp == nums[idx]:
        #             return [i, idx]

        # -> 2
        # O(N^2)
        # for i in range(len(nums)):
        #     a = target - nums[i]
        #     a_idx = nums.index(a)
        #     if a in nums and i != a_idx:
        #         return [i, a_idx]

        # -> 3
        # O(N)
        pair_idx = {}

        for idx, val in enumerate(nums):
            if target - val in pair_idx:
                return [idx, pair_idx[target - val]]
            pair_idx[val] = idx


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))

# ( for a in range(i + 1, len(nums)): ) " i "dan 1ci indexdagi soni yoki holagan indexdagi soni oladi ca
# " a "da " i " digidan 1ta index oldinda yuradi. Chunki bular " range() "ning ichiga yozilvoti.
# https://leetcode.com/problems/two-sum/submissions/
