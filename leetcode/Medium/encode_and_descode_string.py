from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""

        res = ""
        for i in strs:
            res += str(len(i)) + "$" + i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        left = 0

        while left < len(s):
            # # 3$yes
            right = left  # move right to start of the next word collection (3$yes, 4$help)
            while s[right] != "$":
                # # move right to $
                right += 1  # run until find special symbol
            # # cut 3 from 3$yes - 3 $yes
            length = int(s[left:right])  # after run, we have correct left and right, next original word is in between left and right
            # # left position in "y" from yes
            left = right + 1  # left - idx, right - $ symbol. We move left into start position of original word
            # # right position in "s" from yes
            right = left + length  # end idx of the original word. length - len (idx) of original word fex: 1$ - 1, 3$ - 3
            # # append word from y to s -> yes
            res.append(s[left:right])
            # # move left to next idx
            left = right  # move left to next idx (length of original word)

        return res


if __name__ == '__main__':
    sol = Solution()
    # result = sol.encode(["neet", "code", "love", "you"])
    # result = sol.encode([])
    result = sol.encode(["we", "say", ":", "yes", "!@#$%^&*()"])
    print('encode: ', result)
    print('decode: ', sol.decode(result))


#
# https://leetcode.com/problems/encode-and-decode-strings/
# https://neetcode.io/problems/string-encode-and-decode?list=neetcode150
