class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        l = []
        for i in nums:
            count = 0
            for j in nums:
                if i > j:
                    count += 1
            l.append(count)
        return l


if __name__ == '__main__':
    nums = [6, 5, 4, 8]
    print(Solution().smallerNumbersThanCurrent(nums))

# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
#

