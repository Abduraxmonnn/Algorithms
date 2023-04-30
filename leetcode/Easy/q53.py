class Solution(object):
    def maxSubArray(self, nums):
        total = nums[0]
        curr_sum = 0

        for i in nums:
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += i

            total = max(total, curr_sum)

        return total


if __name__ == '__main__':
    nums = [5, 4, -1, 7, 8, -2]
    print(Solution().maxSubArray(nums))

#
#
# https://leetcode.com/problems/maximum-subarray/

# new_list = []
#
# if len(nums) > 5:
#     f = 0
#     s = 4
#     for i in range(len(nums)):
#         new_list.append(nums[f:s])
#         f += 1
#         s += 1
#
#     for j in range(len(new_list)):
#         max_l = max(new_list[j])
#
#         # print(max_l)
#         return sum(new_list[max_l - 1])
# elif len(nums) == 5:
#     return sum(nums)
# elif len(nums) <= 4:
#     for i in nums:
#         if i >= 0:
#             return sum(nums)
#         else:
#             return max(nums)
# else:
#     return sum(nums)
#
