class Solution(object):
    def hammingWeight(self, n):
        return bin(n).count("1")

#
#
# https://leetcode.com/problems/number-of-1-bits/
