class Solution:
    def rob(self, nums):
        if len(nums) < 3:
            return max(nums)

        amount = [nums[0], nums[1], nums[0] + nums[2]]

        if len(nums) < 4:
            return max(amount)

        for i in range(3, len(nums)):
            next_max = max(amount[i - 2], amount[i - 3]) + nums[i]
            amount.append(next_max)

        return max(amount)


if __name__ == '__main__':
    nums = [1, 1, 1, 3, 2, 1]
    print(Solution().rob(nums))


#
#
# https://leetcode.com/problems/house-robber/

# - 1chi amount 3tali listdi javobi oladi va javobi list ohiriga yozadi agar 3tadan kotta bosa list for ga kirib 4chi indexdan
# boshlab ketadi va next_max da toq indexdigi yoki juft indexdi sonlani oliwi tewiradi max()da va owa songa num[i] qoshib
# obshiy agar toq yoki juft indexdildigi sonlar yig'indilarini qowib ketadi va ohirgi returnda qaysi biridan bowlaganda
# (juft yoki toq) kotta summa chiqshini talidi max() orqali.
# - list kota bop ketmidi amout list nums listdaka uzunlida boladi prosta amoutda juft va toq indexladan (uyladan) yurganda
# kopro son (pul) chiqsh mumkin bogan sonlarni (pulani) numsning 3chi indexdan bowlab hisoblab ketadi.
# - numsning 3chi indexsidan boshlab next_max da talangan max son numsdi indexlar (4 5 6...)lar orniga qowilib ketadi
# - qowiliw amount listda turgan [i-2] va [i-3] sonladan max talab hozirgi [i] songa qowib fordi gali kegan index (i) ni
# orniga yozib ketadi

# tepada yozilgan gaplaga cuniw qiyin bosa debug yoki prosta codeni oqib cuniw mumkin )
