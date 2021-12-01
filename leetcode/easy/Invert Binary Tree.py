from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def invertTree(self, root):
        if root:
            root.left, root.right = (self.invertTree(root.right),
                                     self.invertTree(root.left))
            return root

n2 = TreeNode(7)
n1 = TreeNode(2)
n = TreeNode(4, n1, n2)


def nel(root):

    if not root:
        return

    print(root.val)
    nel(root.left)
    nel(root.right)


nel(n)