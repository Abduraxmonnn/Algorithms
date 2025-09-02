class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        # # -> 1
        # # O(N^2)
        # result = []
        #
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[i] != nums[j] and nums[j] < nums[i]:
        #             count += 1
        #     result.append(count)
        #
        # return result

        # -> 2
        # O(n log n)
        count = dict()
        for index, value in enumerate(sorted(nums)):
            if value not in count:
                count[value] = index

        result = [count[value] for value in nums]
        return result


if __name__ == '__main__':
    nums = [8, 1, 2, 2, 3]  # [4,0,1,1,3]
    # nums = [6, 5, 4, 8]  # [2,1,0,3]
    # nums = [7, 7, 7, 7]  # [0,0,0,0]
    print(Solution().smallerNumbersThanCurrent(nums))

#
#
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
