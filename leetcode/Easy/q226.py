# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        if root is None:
            return root

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


if __name__ == "__main__":
    root = [4, 2, 7, 1, 3, 6, 9]
    print(Solution().invertTree(root))


#
#
# https://leetcode.com/problems/invert-binary-tree/submissions/842661952/
