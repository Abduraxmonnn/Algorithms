class Solution(object):
    def finalValueAfterOperations(self, operations):
        res = 0

        for asd in operations:
            if "-" in asd:
                res -= 1
            else:
                res += 1
        return res


if __name__ == '__main__':
    operations = ["X++", "++X", "--X", "X--"]
    print(Solution().finalValueAfterOperations(operations))
