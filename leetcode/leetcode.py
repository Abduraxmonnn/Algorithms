# class Solution:
#     def nthUglyNumber(self, n: int):
#         res = []
#
#         if n == 1:
#             return 1
#
#         for i in range(0, 1690):
#             if len(res) < n:
#                 if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
#                     res.append(i)
#         return res
#
#
# if __name__ == '__main__':
#     n = 11
#     print(Solution().nthUglyNumber(n))

class Solution:
    def reverseVowels(self, s: str):
        for i in range(len(s)):
            vowels = ['a', 'e', 'i', 'o', 'u']
            hold = ''
            if s[i] in vowels:
                s[i] = hold

                hold += s[i]
                print(s[i])
            print(hold)


if __name__ == '__main__':
    s = 'leetcode'
    print(Solution().reverseVowels(s))
