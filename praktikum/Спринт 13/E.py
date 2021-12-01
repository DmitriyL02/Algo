# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def is_binary_search_tree(self, root, left, right) -> bool:

        if not root:
            return True

        if root.value >= right or root.value <= left:
            return False

        left = self.is_binary_search_tree(root.left, left, root.value)
        right = self.is_binary_search_tree(root.right, root.value, right)

        return left and right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_binary_search_tree(root, float('-inf'), float('inf'))
