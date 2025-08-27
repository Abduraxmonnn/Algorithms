class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    x = 121
    print(Solution().isPalindrome(x))


#
# https://leetcode.com/problems/palindrome-number/
