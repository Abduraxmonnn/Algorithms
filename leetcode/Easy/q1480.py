class Solution(object):
    def runningSum(self, nums):
        # -> 1
        for a in range(1, len(nums)):
            nums[a] += nums[a - 1]
        return nums

        # -> 2
        # step = 0
        # result = []
        #
        # for i in nums:
        #     step += i
        #     result.append(step)
        #
        # return result


if __name__ == '__main__':
    nums = [3, 1, 2, 10, 1]
    print(Solution().runningSum(nums))

# 4chi qator / index boylab yurib 1ci indexga undan olldingi indexdagi soni qowaman (nums[a-1])
# len() функция возвращает количество элементов объекта.
# Отсутствие передачи аргумента или передача недопустимого аргумента вызовет TypeError исключение.
# https://leetcode.com/problems/running-sum-of-1d-array/
