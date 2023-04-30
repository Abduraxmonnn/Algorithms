class Solution(object):
    def isAdditiveNumber(self, num):
        lst_num = []

        lst_f = []
        lst_s = []
        lst_p = []

        lst_plus = []
        lst_compare = []

        for i in range(len(num)):
            lst_num.append(num[i])

        for i in range(0, len(lst_num)-2):
            lst_f.append(lst_num[i])

        for i in range(1, len(lst_num)-1):
            lst_s.append(lst_num[i])

        for i in range(2, len(lst_num)):
            lst_compare.append(lst_num[i])

        for i in range(len(lst_f)):
            lst_p.append(int(lst_f[i]) + int(lst_s[i]))

        a = ''.join(map(str, lst_p))

        for i in range(len(a)):
            lst_plus.append(a[i])

        for i in range(len(lst_compare)):
            if lst_compare == lst_plus:
                return True
            else:
                return False


if __name__ == '__main__':
    num = "112358"
    print(Solution().isAdditiveNumber(num))


#
#
# https://leetcode.com/problems/additive-number/