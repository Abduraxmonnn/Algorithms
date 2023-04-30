class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        while k < len(nums):
            if nums[k] == val:
                nums.remove(val)
                continue
            k += 1
        return k


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(Solution().removeElement(nums, val))


# https://leetcode.com/problems/remove-element/
