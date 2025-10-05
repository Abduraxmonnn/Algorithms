class Solution(object):
    def isAnagram(self, s, t):
        # -> 1
        # O(N)
        if len(s) != len(t):
            return False

        t_list = list(t)

        for char in s:
            if char not in t_list:
                return False
            t_list.remove(char)

        return True

        # # -> 2
        # # O(N)
        # if len(s) != len(t):
        #     return False
        #
        # l_map = {}
        # for char in t:
        #     l_map[char] = l_map.get(char, 0) + 1
        #
        # for char in s:
        #     if char not in t or l_map[char] == 0:
        #         return False
        #     l_map[char] -= 1
        # return True

        # # -> 3
        # # O(n log n)
        # if sorted(list(s)) == sorted(list(t)):
        #     return True
        # return False
        # 2.2
        # return Counter(s) == Counter(t)

        # # OLD
        # l_s = []
        # l_t = []
        #
        # if len(s) == len(t):
        #     c = 0
        #     while len(s) != len(l_s):
        #         l_s.append(s[c])
        #         l_t.append(t[c])
        #
        #         c += 1
        # else:
        #     return False
        #
        # if sorted(l_s) == sorted(l_t):
        #     return True
        # else:
        #     return False


if __name__ == '__main__':
    s = "a"
    t = "ab"
    print(Solution().isAnagram(s, t))

#
#
# https://leetcode.com/problems/valid-anagram/
