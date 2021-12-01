# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        node = self

        while node:
            if node.value < value:
                if not node.left:
                    node.left = BST(value)
                    break
                node = node.left
            elif node.value >= value:
                if not node.right:
                    node.right = BST(value)
                    break
                node = node.right

        return self

    def contains(self, value):

        node = self

        while node:

            if node.value < value:
                node = node.right
            elif node.value > value:
                node = node.left
            else:
                return True

        return False

    def remove(self, value, parentNode=None):

        node = self

        while node:

            if value < node.value:
                parentNode = node
                node = node.left
            elif value > node.value:
                parentNode = node
                node = node.right
            else:
                if node.left and node.right:
                    node.value = node.right.get_min_value()
                    node.right.remove(node.value, node)
                elif parentNode is None:
                    if node.left:
                        node.value = node.left.value
                        node.right = node.left.right
                        node.left = node.left.left
                    elif node.right:
                        node.value = node.right.value
                        node.left = node.right.left
                        node.right = node.right.right
                    else:
                        pass
                elif parentNode.left is node:
                    parentNode.left = node.left if node.left else node.right
                elif parentNode.right is node:
                    parentNode.right = node.left if node.left else node.right

                break

        return self

    def get_min_value(self):

        node = self

        while node.left:
            node = node.left
        return node.value
