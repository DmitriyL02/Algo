# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    branchSumsHelper(root, 0, sums)

    return sums


def branchSumsHelper(root, memory, sums):

    if root is None:
        return

    memory = memory + root.value

    if root.left is None and root.right is None:
        sums.append(memory)
        return

    branchSumsHelper(root.left, memory, sums)
    branchSumsHelper(root.right, memory, sums)
