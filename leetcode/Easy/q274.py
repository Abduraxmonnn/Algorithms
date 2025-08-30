from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        :type citations: List[int]
        :rtype: int
        """
        # -> 1
        # 0(n log n)
        citations.sort(reverse=True)
        n = len(citations)
        h_index = 1

        for item in range(len(citations)):
            if citations[item] < h_index:
                return h_index - 1
            h_index += 1

        return n

        # # -> 1.1
        # # 0(n log n)
        # citations.sort(reverse=True)
        # for i in range(len(citations)):
        #     if i >= citations[i]:
        #         return i
        # return len(citations)

        # # -> 2
        # # 0(n^2)
        # for outer in range(1, len(citations)):
        #     count = 0
        #     for inner in range(len(citations)):
        #         if citations[inner] >= outer:
        #             count += 1
        #
        #     if count < outer:
        #         return outer - 1

        # # -> 3 (no)
        # count = 0
        # h = 1
        # for item in range(len(citations)):
        #     if citations[item] >= item:
        #         count += 1
        #
        #     if count == h:
        #         h += 1
        #         count = 0
        #
        # return h

        # # -> 4 (not entirely clear)
        # # O(n log n)
        # n = len(citations)
        # citations.sort()
        #
        # for i, v in enumerate(citations):
        #     if n - i <= v:
        #         return n - i
        # return 0


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]  # 3
    # citations = [1, 3, 1]  # 1
    # citations = [100]  # 1
    # citations = [4, 7, 6, 1, 9, 12]  # 4
    print(Solution().hIndex(citations))

#
#
# https://leetcode.com/problems/h-index/
