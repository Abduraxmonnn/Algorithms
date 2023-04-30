class Solution(object):
    def plusOne(self, digits):
        convert = int("".join(map(str, digits)))
        return list(str(convert+1))


if __name__ == '__main__':
    digits = [1, 2, 3]
    print(Solution().plusOne(digits))
