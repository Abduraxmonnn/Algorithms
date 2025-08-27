class Solution(object):
    def restoreString(self, s, indices):
        a = list(s)
        for i in range(len(indices)):
            a[indices[i]] = s[i]
        return "".join(a)


if __name__ == '__main__':
    s = 'aaiougrt'
    indices = [4, 0, 2, 6, 7, 3, 1, 5]
    print(Solution().restoreString(s, indices))


# join() = Метод принимает итератор (объекты , способные возвращать его членов по одному за раз) в качестве параметра.
# in Algorithm Telegram channel
# https://leetcode.com/problems/shuffle-string/
