class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left


def print_range(node: Node, l: int, r: int) -> None:
    ...