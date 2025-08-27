from collections import Counter


class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        # -> 1
        # count = Counter(stones)
        # total = 0
        # for i in jewels:
        #     if i in count:
        #         total += count[i]
        # return total

        # -> 2
        jewels_count = 0
        for j in stones:
            if j in jewels:
                jewels_count += 1

        return jewels_count


if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"
    print(Solution().numJewelsInStones(jewels, stones))

# (count = Counter(stones))hama towlani hisoblab(sanab) chiqadi va (for i in jewels) bza uchun jewelsdagi hama
# narsani harflani yokida towlarni tekwirib beradi va kein (if i in count) orqali i(jewels)dagi narsalani hisoblab
# chiqamz agar stonestda jewelsda bor narsala bosa (total = 0)ga qowb ketamz (total += count[i]) kodi orqali

# https://leetcode.com/problems/jewels-and-stones/
