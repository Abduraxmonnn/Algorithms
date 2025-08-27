# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#

# class Solution(object):
#     def isSameTree(self, p, q):
#         if len(p) != len(q):
#             return "false"
#         # for i in p:
#         #     print(i)
#
#         for i in p:
#             for j in q:
#                 if p[i] == q[j]:
#                     return "true"
#                 else:
#                     return "false"
#

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


if __name__ == '__main__':
    p = [1, 2, 1]
    q = [1, 1, 2]
    print(Solution().isSameTree(p, q))
