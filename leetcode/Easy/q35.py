class Solution(object):
    def searchInsert(self, nums, target):
        count, b = 0, len(nums) - 1
        while count <= b:
            mid = int((count + b) / 2)
            if nums[mid] < target:
                count = mid + 1
            else:
                b = mid - 1
        return count


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 7
    print(Solution().searchInsert(nums, target))

#
#
# https://leetcode.com/problems/search-insert-position/


# class Solution(object):
#     def searchInsert(self, nums, target):
#         for i in nums:
#             if target == i:
#                 print(nums[i])
#             else:
#                 for a in nums:
#                     if target < a:
#                         nums.append(target)
