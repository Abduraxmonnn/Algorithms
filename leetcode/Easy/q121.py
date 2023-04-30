class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit


if __name__ == '__main__':
    prices = [7, 2, 5, 1, 3, 6, 4]
    print(Solution().maxProfit(prices))


#
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# 1)
# min qiymat bowida prices[0] (min_price) turadi va man kein undan keingi indexda turgan sonlani (range(1, len(prices)))
# soliwtirib uladan min qiymatini talab ketaman. Boshida default prices[0] minimum price boladi

# 2)
#  """range(1, len(prices))""" nimaga 1chi indexdan boshlavoman chunki tepada min_price 0chi indexga teng agar man 0 dan
# min check qvokanda 0chi indexdi sonlarni bir-biri bn soliwtirgan bolardi (min_price = prices[0] bn prices[i] (i=0) bir xl narsa 2 lasi)
# shunga 1 dan bowladi. 0chi (min_price) bn 1chi indexdi soni solishtirib min qiymatni olish uchun

# Qolganlani debug qilib chunvolish mumkin
