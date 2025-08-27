class Solution(object):
    def lengthOfLastWord(self, s):
        elements = s.split()
        remove = elements[-1]
        return len(remove)


if __name__ == '__main__':
    s = "   fly me   to   the moon  "
    print(Solution().lengthOfLastWord(s))

#
#
# https://leetcode.com/problems/length-of-last-word/
