import re


class Solution(object):
    # -> 3
    # T: O(n) - M: O(1)
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.isalphanum(s[left]):
                left += 1

            while left < right and not self.isalphanum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    def isalphanum(self, s: str) -> bool:
        return (
                ord("0") <= ord(s) <= ord("9")
                or
                ord("A") <= ord(s) <= ord("Z")
                or
                ord("a") <= ord(s) <= ord("z")
        )

    # # -> 2
    # # T: O(n) - M: O(n)
    #     filtered = "".join(filter(str.isalnum, s)).lower()
    #
    #     return filtered == filtered[::-1]

    # -> 1
    #     s = re.sub("[^a-z|^0-9]", "", s.lower())
    #     org, reverse = 0, len(s) - 1
    #
    #     while org < reverse:
    #         if s[org] != s[reverse]:
    #             return False
    #         org += 1
    #         reverse -= 1
    #     return True


if __name__ == '__main__':
    s = "0P"
    # s = "Was it a car or a cat I saw?"
    # s = "tab a cat"
    # s = "."
    # s = "No lemon, no melon"
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
# https://www.youtube.com/watch?v=76g27yVqlYo
# https://leetcode.com/problems/valid-palindrome/
