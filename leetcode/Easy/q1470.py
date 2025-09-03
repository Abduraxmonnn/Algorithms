class Solution(object):
    def shuffle(self, nums, n):
        # -> 1
        # O(N)
        res = []

        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res

        # # -> 2
        # # O(N)
        # second_n = []
        #
        # first_point = 0
        # second_point = n
        # ln = len(nums) - 1
        #
        # while second_point <= ln:
        #     second_n.append(nums[first_point])
        #     second_n.append(nums[second_point])
        #     first_point += 1
        #     second_point += 1
        #
        # return second_n


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    print(Solution().shuffle(nums, n))

# num массивdan 1chi indexdan "n"ta index keingilarini qowib = ( es.append(nums[i+n]) )
# jovob (res) массивni toldirvoman chqarvoman
# https://leetcode.com/problems/shuffle-the-array/
