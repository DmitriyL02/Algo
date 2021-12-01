def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)


def findClosestValueInBstHelper(tree, target, memory):
    # Write your code here.

    if tree is None:
        return memory

    if abs(target - memory) > abs(target - tree.value):
        memory = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, memory)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, memory)
    else:
        return memory


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
