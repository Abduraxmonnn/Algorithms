from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head
        if head.next is None:
            return head

        p = head
        q = head.next
        r = head.next.next
        p.next = None

        if r is None:
            p.next = None
            q.next = head
            return q

        while r is not None:
            q.next = p
            p = q
            q = r
            r = r.next
        q.next = p
        return q


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    print(Solution().reverseList(head))


#
#
# https://leetcode.com/problems/reverse-linked-list/


# class Solution(object):
#     def reverseList(self, head):
#         new_l = []
#         last = -1
#
#         for i in range(len(head)):
#             new_l.insert(last, head[i])
#             last -= 1
#         return new_l
#
# if __name__ == '__main__':
#     head = [1, 2, 3, 4, 5]
#     print(Solution().reverseList(head))


# head[::-1]
