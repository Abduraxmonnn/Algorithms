class Solution(object):
    def finalValueAfterOperations(self, operations):
        # -> 1
        # O(n)
        init_value = 0

        for i in operations:
            if '-' in i:
                init_value -= 1
            else:
                init_value += 1

        return init_value

        # # -> 2
        # # O(n)
        # return sum(1 if '+' in i else -1 for i in operations)

        # # -> 3
        # # O(n)
        # possible_variants = {'X++': 1, '++X': 1, 'X--': -1, '--X': -1}
        # init_value = 0
        #
        # for i in operations:
        #     init_value += possible_variants[i]
        # return init_value


if __name__ == '__main__':
    # operations = ["--X", "X++", "X++"]  # 1
    operations = ["++X", "++X", "X++"]  # 3
    # operations = ["X++", "++X", "--X", "X--"]  # 0
    print(Solution().finalValueAfterOperations(operations))

#
#
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
