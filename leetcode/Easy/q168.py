class Solution(object):
    def convertToTitle(self, columnNumber):
        result = ''

        while columnNumber > 0:
            # find the index of the next letter and concatenate the letter
            # to the solution

            # here index 0 corresponds to `A`, and 25 corresponds to `Z`
            index = (columnNumber - 1) % 26
            result += chr(index + ord('A'))
            columnNumber = (columnNumber - 1) // 26

        return result[::-1]


if __name__ == '__main__':
    columnNumber = 1
    print(Solution().convertToTitle(columnNumber))


#
#
# https://leetcode.com/problems/excel-sheet-column-title/
