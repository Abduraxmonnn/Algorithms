class Solution(object):
    def isAnagram(self, s, t):
        l_s = []
        l_t = []

        if len(s) == len(t):
            c = 0
            while len(s) != len(l_s):
                l_s.append(s[c])
                l_t.append(t[c])

                c += 1
        else:
            return False

        if sorted(l_s) == sorted(l_t):
            return True
        else:
            return False


if __name__ == '__main__':
    s = "a"
    t = "ab"
    print(Solution().isAnagram(s, t))


#
#
# https://leetcode.com/problems/valid-anagram/

# l_s = []
# l_t = []
#
# for i in range(0, len(s)):
#     l_s.append(s[i])
#
# for j in range(0, len(t)):
#     l_t.append(t[j])
#
# if sorted(l_s) == sorted(l_t):
#     return True
# else:
#     return False
