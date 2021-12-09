# This is an input class. Do not edit.
from collections import deque


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):

    def validateBstHelper(tree, min_value, max_value):

        if tree is None:
            return True
        elif tree.value < min_value or tree.value >= max_value:
            return False

        return (validateBstHelper(tree.left, min_value, tree.value)
                and validateBstHelper(tree.right, tree.value, max_value))

    return validateBstHelper(tree, float('-inf'), float('inf'))

