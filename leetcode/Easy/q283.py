class Solution(object):
    def moveZeroes(self, nums):
        pos = 0

        for i in range(len(nums)):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

        return nums


if __name__ == '__main__':
    nums = [9, 4, 0, 2, 1, 0, 3, 12]
    print(Solution().moveZeroes(nums))


#
#
# https://leetcode.com/problems/move-zeroes/

# lst = []
#
# for j in range(len(nums)):
#     if 0 != nums[j]:
#         lst.append(nums[j])
#
# for i in range(len(nums)):
#     if 0 == nums[i]:
#         lst.append(nums[i])
#
# return lst


# for - bu obshiy index boyicha ketadi lekin "pos" bu 0 bolmagan sonlarni indexi bolib agar "for" bilan "pos" indexlari
# orasida qanaqdur farqi kesa osha far orasida "0" bogan boladi agar 2ta "0" chiqsa "for" va "pos" indexlari 2taga
# farq qiladi va "0" toplgandan keyin != 0 shunaqa son chiqsa shu son bilan "pos" indexdigi son aniqrogi "0" bilan oz
# joylarini almashadi. Agar ja chunmasin ozin kodi miyenda debug qilib kor yoki PyCharm debug dan foydalanb

# append, remove lar ishlatish mumkin bomagani uchun man ozimi codimi ishlatomadim
