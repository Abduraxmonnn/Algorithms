from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # -> 1
        # O(N log n)
        frequent = {}
        res = []

        for i in nums:
            if i in frequent:
                frequent[i] += 1
            else:
                frequent[i] = 1

        # most_frequent works logic: get last k items from frequent
        # 1) frequent = {1: 3, 2: 2, 3: 1}
        # 2) get values and convert to list -> [3, 2, 1]
        # 3) sorting by values - most frequent nums (its value of frequent) -> [1, 2, 3]
        # 4) get last k elements from sorted by values list -> [1, 2, 3] will be [2, 3]
        most_frequent = sorted(list(frequent.values()))[-k:]
        for key, val in frequent.items():
            if val in most_frequent:
                res.append(key)

        return res


if __name__ == '__main__':
    # nums = [1, 2, 2, 3, 3, 3]
    # k = 2
    # nums = [7, 7]
    # k = 1
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    # nums = [3, 0, 1, 0]
    # k = 1
    print(Solution().topKFrequent(nums, k))

#
#
# https://leetcode.com/problems/top-k-frequent-elements/
