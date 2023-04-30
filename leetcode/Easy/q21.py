# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next


if __name__ == '__main__':
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    print(Solution().mergeTwoLists(list1, list2))


#
#
# https://leetcode.com/problems/merge-two-sorted-lists/
