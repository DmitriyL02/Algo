# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def counting(self, node) -> int:

        if not node:
            return 0

        else:
            return self.counting(node.left) + self.counting(node.right) + 1

    def countNodes(self, root) -> int:
        return self.counting(root)


lst = []


def counting(node) -> int:
    if not node:
        return 0

    return counting(node.left) + counting(node.right) + 1


# [1,2,3,4,5,6]

f = TreeNode(6)
e = TreeNode(5)
d = TreeNode(4)
c = TreeNode(3, f)
b = TreeNode(2, d, e)
a = TreeNode(1, b, c)

print(counting(a))



