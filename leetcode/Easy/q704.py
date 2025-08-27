class Solution(object):
    def search(self, nums, target):
        step = 0

        if target not in nums:
            return -1

        for i in range(len(nums)):
            if nums[i] == target:
                return step
            step += 1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(Solution().search(nums, target))


#
#
# https://leetcode.com/problems/binary-search/
