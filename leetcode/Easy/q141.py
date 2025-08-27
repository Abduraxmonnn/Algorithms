# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False

        slow = fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False


#
#
# https://leetcode.com/problems/linked-list-cycle/

# fast.next.next -- fast 2ta qadamdan yuradi 
# slow.next -- slow 1ta qadandan yuradi
# agar fast 2tadan yurb slowga yetb kesa (fast==slow) True boladi

# https://youtu.be/k2DP9Gd13F4   ----> FOR MORE
