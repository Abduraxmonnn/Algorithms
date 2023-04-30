class Solution:
    def addDigits(self, n):
        while n > 9:
            a = list(map(int, str(n)))
            n = sum(a)
        return n


if __name__ == '__main__':
    num = 38
    print(Solution().addDigits(num))
