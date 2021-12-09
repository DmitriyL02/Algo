def inOrderTraverse(tree, array):
    # Write your code here.
    def inOrderTraverseHelper(tree):
        if not tree:
            return

        inOrderTraverseHelper(tree.left)
        array.append(tree.value)
        inOrderTraverseHelper(tree.right)

    inOrderTraverseHelper(tree)

    return array


def preOrderTraverse(tree, array):
    # Write your code here.

    def preOrderTraverseHelper(tree):
        if not tree:
            return

        array.append(tree.value)
        preOrderTraverseHelper(tree.left)
        preOrderTraverseHelper(tree.right)

    preOrderTraverseHelper(tree)

    return array


def postOrderTraverse(tree, array):
    # Write your code here.
    def postOrderTraverseHelper(tree):
        if not tree:
            return

        postOrderTraverseHelper(tree.left)
        postOrderTraverseHelper(tree.right)
        array.append(tree.value)

    postOrderTraverseHelper(tree)

    return array
