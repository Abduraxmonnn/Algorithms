from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # -> 1
        # # Time: O(n (m log m)) = n(m log m)
        # # Space: O(n * m)
        # res = []
        # proceed = []
        #
        # if strs == "":
        #     return [strs]
        #
        # for i in range(len(strs)):
        #     if strs[i] not in proceed:
        #         tmp_res = [strs[i]]
        #         proceed.append(strs[i])
        #         for j in range(i + 1, len(strs)):
        #             if Counter(strs[i]) == Counter(strs[j]):
        #                 tmp_res.append(strs[j])
        #                 proceed.append(strs[j])
        #         res.append(tmp_res)
        #
        # return res

        # # -> 2
        # # Time: O(n * m)
        # anagrams_dict = defaultdict(list)  # mapping charCount to list of Anagrams
        #
        # for word in strs:
        #     count = [0] * 26
        #     for letter in word:
        #         count[ord(letter) - ord('a')] += 1
        #
        #     key = tuple(count)
        #     anagrams_dict[key].append(word)
        #
        # return list(anagrams_dict.values())

        # -> 3
        # O(n * m)
        groups = defaultdict(list)
        # groups will work like:
        # act -> act -> {act: [act]}
        # cat -> act -> {act: [act, cat]}
        # tac -> act -> {act: [act, cat, tac]}
        for word in strs:

            key = "".join(sorted(word))  # sorted save as list, we need str

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())


if __name__ == '__main__':
    # strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # strs = ["x"]
    # strs = [""]
    # strs = ["", ""]
    print(Solution().groupAnagrams(strs))

#
#
# https://leetcode.com/problems/group-anagrams/
