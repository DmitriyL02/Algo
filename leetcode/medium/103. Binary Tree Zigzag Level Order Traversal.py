from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque([root])
        output = []
        counter = 0

        while queue:

            tmp_output = []

            for _ in range(len(queue)):

                node = queue.popleft()

                if node:

                    tmp_output.append(node.val)

                    if node.right:
                        queue.append(node.right)

                    if node.left:
                        queue.append(node.left)

            if tmp_output:
                output += [tmp_output]

        return output


node4 = TreeNode(7)
node3 = TreeNode(15)
node2 = TreeNode(20, node3, node4)
node1 = TreeNode(9)
node = TreeNode(3, node1, node2)

print(Solution().zigzagLevelOrder(node))