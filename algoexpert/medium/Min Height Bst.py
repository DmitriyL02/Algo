from typing import List, Optional


def minHeightBst(array: List):

    def minHeightBstHelper(arr: List[int], tree: Optional[BST], start: int,
                           end: int) -> Optional[BST]:

        if end < start:
            return

        middle = (start + end) // 2
        value = arr[middle]

        if not tree:
            tree = BST(value)
        else:
            tree.insert(value)

        minHeightBstHelper(arr, tree, start, middle - 1)
        minHeightBstHelper(arr, tree, middle + 1, end)

        return tree

    return minHeightBstHelper(array, None, 0, len(array) - 1)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)