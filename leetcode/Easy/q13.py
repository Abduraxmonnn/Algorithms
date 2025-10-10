class Solution(object):
    def romanToInt(self, s):
        # -> 1
        # TC: O(N)
        # SC: o(1)
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0

        for i in s[::-1]:
            if symbols[i] >= prev:
                total += symbols[i]
            else:
                total -= symbols[i]
            prev = symbols[i]

        return total

        # # -> 2
        # # TC: O(N)
        # # SC: o(1)
        # symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # s_list = list(reversed(s))
        # total = symbols[s_list[0]]
        # prev = symbols[s_list[0]]
        #
        # for i in range(1, len(s_list)):
        #     crt = s_list[i]
        #     if symbols[crt] >= prev:
        #         total += symbols[crt]
        #         prev = symbols[crt]
        #     else:
        #         total -= symbols[crt]
        #         prev = symbols[crt]
        #
        # return total


if __name__ == '__main__':
    # s = "III"  # 3
    # s = 'LVIII'  # 58
    # s = 'MCMXCIV' # 1994
    s = "IV"  # 4
    print(Solution().romanToInt(s))

#
# https://leetcode.com/problems/roman-to-integer/
