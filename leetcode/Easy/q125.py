import re


class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-z|^0-9]", "", s.lower())
        org, reverse = 0, len(s) - 1

        while org < reverse:
            if s[org] != s[reverse]:
                return False
            org += 1
            reverse -= 1
        return True


if __name__ == '__main__':
    s = "0P"
    print(Solution().isPalindrome(s))

# s = "".join(i for i in s if i.isalpha())
# org = s.lower()
# reverse = s[::-1].lower()
#
# if org == reverse:
#     return "true"
# else:
#     return "false"

# org - "s"ni 1chi elementidan. reverse - "s"ni ohrigi -1 elementidan hisoblidi.

#
#
# https://leetcode.com/problems/valid-palindrome/
