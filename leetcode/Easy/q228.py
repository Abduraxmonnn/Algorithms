class Solution:
    def summaryRanges(self, nums):
        res = list()
        j = 0
        if len(nums) == 0:
            return nums
        if len(nums) == 1:
            y = nums[0]
            res.append(str(y))
            return res

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                continue
            if j == i - 1:
                x = f"{str(nums[j])}"
            else:
                x = f"{str(nums[j])}->{str(nums[i - 1])}"
            j = i
            res.append(x)

        if j == i:
            x = f"{str(nums[i])}"
        else:
            x = f"{str(nums[j])}->{str(nums[i])}"
        res.append(x)

        return res


if __name__ == '__main__':
    # nums = [0, 1, 2, 4, 5, 7]
    nums = [0, 2, 3, 4, 6, 8, 10, 12, 13]
    print(Solution().summaryRanges(nums))

#
#
# https://leetcode.com/problems/summary-ranges/
