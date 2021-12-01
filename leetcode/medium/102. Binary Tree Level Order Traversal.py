from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        answer = []
        q = deque([root])

        while q:

            depth_values = []
            depth_length = len(q)

            for _ in range(depth_length):

                node = q.popleft()

                if node:
                    depth_values.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if depth_values:
                answer += [depth_values]

        return answer


f = TreeNode(7)
e = TreeNode(15)
c = TreeNode(20, e, f)
b = TreeNode(9)
a = TreeNode(3, b, c)

print(Solution().levelOrder(a))
