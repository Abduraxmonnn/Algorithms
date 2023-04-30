class Solution(object):
    def countConsistentStrings(self, allowed, words):
        res = 0

        for a in words:
            for i in a:
                if i not in allowed:
                    res += 1
        return len(words) - res


if __name__ == '__main__':
    allowed = "abc"
    words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
    print(Solution().countConsistentStrings(allowed, words))


#
#
# https://leetcode.com/problems/count-the-number-of-consistent-strings/
