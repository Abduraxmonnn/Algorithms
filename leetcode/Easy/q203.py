class Solution(object):
    def removeElements(self, head, val):
        new_l = []

        for i in head:
            if head[i] == val:
                head.remove(val)

        for j in range(len(head)):
            new_l.append(head[j])

        new_l.append(val)
        return new_l


if __name__ == '__main__':
    head = [1, 2, 6, 3, 4, 5, 6]
    val = 6
    print(Solution().removeElements(head, val))


#
#
# https://leetcode.com/problems/remove-linked-list-elements/

# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         # if linkedList is empty
#         if head == None:
#             return head
#         # 2 pointers pointing head
#         current = head
#         prev = head
#         # condition will be on checking next node is null or not to avoid error
#         # related to NoneType
#         while current.next:
#             current = current.next
#             if current.val == val:
#                 prev.next = current.next
#             else:
#                 prev = prev.next
#     # it will check if head matches same value then it will shift head pointer to next untill head.next!= val.
#         if head.val == val:
#             return head.next
#         return head
