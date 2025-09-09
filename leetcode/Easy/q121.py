class Solution(object):
    def maxProfit(self, prices):
        # -> 1
        # O(N)
        buy_price = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
            else:
                tmp_profit = prices[i] - buy_price
                if tmp_profit > profit:
                    profit = tmp_profit

        return profit

        # # -> 2
        # # O(N)
        # min_price = prices[0]
        # max_profit = 0
        #
        # for i in range(1, len(prices)):
        #     min_price = min(min_price, prices[i])
        #     max_profit = max(max_profit, prices[i] - min_price)
        #
        # return max_profit


if __name__ == '__main__':
    prices = [7, 2, 5, 1, 3, 6, 4]
    print(Solution().maxProfit(prices))

#
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
