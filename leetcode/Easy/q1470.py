class Solution(object):
    def shuffle(self, nums, n):
        res = []

        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    print(Solution().shuffle(nums, n))


# num массивdan 1chi indexdan "n"ta index keingilarini qowib = ( es.append(nums[i+n]) )
# jovob (res) массивni toldirvoman chqarvoman
# https://leetcode.com/problems/shuffle-the-array/
