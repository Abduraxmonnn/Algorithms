class Solution(object):
    def titleToNumber(self, columnTitle):
        res = 0
        for i, j in enumerate(reversed(columnTitle)):
            res += (ord(j) - 64) * 26**i
        return res


if __name__ == '__main__':
    columnTitle = "AB"
    print(Solution().titleToNumber(columnTitle))


#
#
# https://leetcode.com/problems/excel-sheet-column-title/

