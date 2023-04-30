class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            hold = s[left]
            s[left] = s[right]
            s[right] = hold
            left += 1
            right -= 1

        return s


if __name__ == '__main__':
    s = ["H", "e", "l", "l", "o"]
    print(Solution().reverseString(s))


    #
    #
    # https://leetcode.com/problems/reverse-string/
