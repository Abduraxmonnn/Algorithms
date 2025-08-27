class Solution(object):
    def sortColors(self, nums):
        ind_len = len(nums) - 1
        sorting = False

        while not sorting:
            sorting = True
            for i in range(0, ind_len):
                if nums[i] > nums[i + 1]:
                    sorting = False
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

        return nums


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    print(Solution().sortColors(nums))


#
#
# https://leetcode.com/problems/sort-colors/

# sorted with Bubble Sort method
