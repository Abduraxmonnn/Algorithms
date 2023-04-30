class Solution(object):
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        lst = []
        for i in s1:
            if i in s2:
                lst.append(i)

        return lst


if __name__ == '__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(Solution().intersection(nums1, nums2))


#
#
# https://leetcode.com/problems/intersection-of-two-arrays/
