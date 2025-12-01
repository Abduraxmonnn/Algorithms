from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # -> 1
        # T: O(N^2)
        # M: O(1)
        # res = []
        #
        # for idx, val in enumerate(numbers):
        #     tmp = target - val
        #     if tmp in numbers:
        #         res.append(idx + 1)
        #         for i in range(idx + 1, len(numbers)):
        #             if i != idx and numbers[i] == tmp:
        #                 res.append(i + 1)
        #
        #         return res

        # -> 2
        # T: O(N)
        # M: O(1)
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if target == total:
                return [left + 1, right + 1]

            if target < total:
                right -= 1
            else:
                left += 1


if __name__ == '__main__':
    # numbers = [2, 7, 11, 15]  # [1, 2]
    # target = 9
    # numbers = [2, 3, 4]  # [1, 3]
    # target = 6
    # numbers = [-1, 0]  # [1, 2]
    # target = -1
    # numbers = [1, 2, 3, 4]  # [1, 2]
    # target = 3
    numbers = [0, 0, 3, 4]  # [1, 2]
    target = 0
    print(Solution().twoSum(numbers, target))

#
#
# YT: https://www.youtube.com/watch?v=PTelHIB4o20
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
