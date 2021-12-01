# Comment it before submitting
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, elem):

    counter = 0
    while node:

        if node.value == elem:
            return counter
        node = node.next_item
        counter += 1

    return -1


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    print(solution(node0, "node4"))
    # result is idx == 2

test()