class Solution(object):
    def wordPattern(self, pattern, s):
        d = {}
        l = s.split()

        if len(pattern) != len(l):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in d:
                if l[i] in d.values():
                    return False
                d[pattern[i]] = l[i]

            else:
                if d[pattern[i]] != l[i]:
                    return False
        return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog dog dog dog"
    print(Solution().wordPattern(pattern, s))

#
#
# https://leetcode.com/problems/word-pattern/

# Didn't submit

# Darabotka qilish kere
#
# if len(set(pattern)) == 1:
#     return False
#
# if len(set(s.split(" "))) == 1:
#     return False
#
# org_lst_pattern = []
# half_lst_pattern = []
# is_pattern = False
#
# for i in range(len(pattern)):
#     org_lst_pattern.append(pattern[i])
#
# for i in range(len(pattern) // 2):
#     half_lst_pattern.append(pattern[i])
#     org_lst_pattern.remove(pattern[i])
#
# if org_lst_pattern[::-1] == half_lst_pattern:
#     is_pattern = True
# else:
#     is_pattern = is_pattern


# s = s.split(" ")
# org_lst_s = []
# half_lst_s = []
# is_s = False
#
# for i in range(len(s)):
#     org_lst_s.append(s[i])
#
# for i in range(len(s) // 2):
#     half_lst_s.append(s[i])
#     org_lst_s.remove(s[i])
#
# if org_lst_s[::-1] == half_lst_s:
#     is_s = True
# else:
#     is_s = is_s
#
# if is_pattern and is_s:
#     return True
# else:
#     return False
