class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        lst = []

        for i in range(len(nums)):
            if lower <= nums[i] <= upper:
                lst.append(nums[i])

        sums = sum(lst)

        return abs(sums)


if __name__ == '__main__':
    nums = [0]
    lower = 0
    upper = 0
    print(Solution().countRangeSum(nums, lower, upper))
