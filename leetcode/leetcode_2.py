class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_count = 0
        for j in stones:
            if j in jewels:
                jewels_count += 1

        return jewels_count


if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"
    print(Solution().numJewelsInStones(jewels, stones))
