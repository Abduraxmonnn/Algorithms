class Solution(object):
    def merge(self, nums1, m, nums2, n):
        new_list = []

        for i in nums1:
            nums1.remove(0)
            new_list.append(i)

        for i in m:
            new_list.append(i)
        new_list.sort()
        nums1 = new_list
        return nums1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(Solution().merge(nums1, nums2, m, n))

#
#
# https://leetcode.com/problems/merge-sorted-array/

"""WORKED in leetcode"""
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         k = m + n - 1
#         while k >= 0:
#
#             # Only test if both a or b are not exhausted
#             if m > 0 and n > 0:
#
#                 # Replaces with the greatest of a
#                 if nums2[n - 1] > nums1[m - 1]:
#                     nums1[k] = nums2[n - 1]
#                     n -= 1
#                 else:
#                     nums1[k] = nums1[m - 1]
#                     m -= 1
#
#                     # If a is exhausted, add the next from b
#             elif m == 0:
#                 nums1[k] = nums2[n - 1]
#                 n -= 1
#
#             # If b is exhausted, add the next from a
#             else:
#                 nums1[k] = nums1[m - 1]
#                 m -= 1
#
#             k -= 1
