class Solution(object):
    def romanToInt(self, s):
        numbers = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900,
                   'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
                   }
        sum = 0

        past = s[-1]

        for n in list(s[::-1]):
            if numbers[n] < numbers[past]:
                sum = sum - numbers[n]
            else:
                sum = sum + numbers[n]
                past = n
        return (sum)


if __name__ == '__main__':
    s = "LVIII"
    print(Solution().romanToInt(s))

#
# https://leetcode.com/problems/roman-to-integer/
