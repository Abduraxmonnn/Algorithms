class Solution(object):
    def strStr(self, haystack, needle):
        # return haystack.index(needle) if needle in haystack else -1
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    print(Solution().strStr(haystack, needle))


#
#
# https://leetcode.com/problems/implement-strstr/


# JAVA (0 ms, 100%faster)

# class Solution {
#     public  int strStr(String haystack, String needle)  {
#         int l = needle.length();
#         for (int i = 0; i < haystack.length() - l+1; i++)  if (haystack.substring(i, i + l).equals(needle)) return i;
#         return haystack.length() == 0 ? 0 : -1;
#     }
# }
