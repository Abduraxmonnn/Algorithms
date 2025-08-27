class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(-1)
        temp = dummy
        carry = 0

        while l1 or l2 or carry:
            s = 0
            if l1:
                s += l1.val
            if l2:
                s += l2.val
            s += carry

            temp.next = ListNode(s % 10)
            temp = temp.next
            carry = s // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    print(Solution().addTwoNumbers(l1, l2))

#
#
# https://leetcode.com/problems/add-two-numbers/

# l1_str = ''.join([str(elem) for elem in l1])
# l2_str = ''.join([str(elem) for elem in l2])
# answer = int(l1_str) + int(l2_str)
# return answer
