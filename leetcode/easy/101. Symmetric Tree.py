# Definition for a binary tree node.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]):
        return self.find_symmetric(root.left, root.right)

    def find_symmetric(self, root1, root2):

        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False

        return self.find_symmetric(root1.left, root2.right) and root1.val == root2.val and self.find_symmetric(root1.right, root2.left)


c = TreeNode(2)
b = TreeNode(2)
a = TreeNode(1, b, c)

print(Solution().isSymmetric(a))