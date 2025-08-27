class Solution(object):
    def containsDuplicate(self, nums):
        lst = []

        for i in range(len(nums)):
            if nums[i] in lst:
                return True
            lst.append(nums[i])

        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(Solution().containsDuplicate(nums))


#
#
# https://leetcode.com/problems/contains-duplicate/

# unique = set(nums)
# for i in unique:
#     nums.remove(i)
#
# if len(nums) != 0:
#     return True
# else:
#     return False

# from LEETCODE (discuss) simple solution
#
# if len(nums) == len(set(nums)):
#     return False
# else:
#     return True
