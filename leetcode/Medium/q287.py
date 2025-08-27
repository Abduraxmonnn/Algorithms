# bu lyuboy len() digi listga ishluradi

class Solution(object):
    def findDuplicate(self, nums):
        count = {}

        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                return i


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    print(Solution().findDuplicate(nums))


#
#
# https://leetcode.com/problems/find-the-duplicate-number/

# Bula kichkinaro unaqa kotaaaaa bomagan listlaga ishlidi lekin kotaaaaaa vasheeee kotalaga ishlamidi len() < 10000 tahminan

# sort = sorted(nums)
#
# for i in range(len(sort)):
#     if nums[i] in nums[i + 1::]:
#         return nums[i]

# lst = []
#
# for i in range(len(nums)):
#     if nums[i] not in lst:
#         lst.append(nums[i])
#     else:
#         return nums[i]
