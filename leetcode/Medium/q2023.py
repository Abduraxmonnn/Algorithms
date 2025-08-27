from itertools import permutations


class Solution(object):
    def numOfPairs(self, nums, target):
        return sum(i + j == target for i, j in permutations(nums, 2))


if __name__ == '__main__':
    nums = ["123", "4", "12", "34"]
    target = "1234"
    print(Solution().numOfPairs(nums, target))


#
#
# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/submissions/
