# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    node = linkedList

    while node is not None:

        next_node = node.next

        while next_node is not None and next_node.value == node.value:
            next_node = next_node.next

        node.next = next_node
        node = next_node



    return linkedList


node = LinkedList(3)
node2 = LinkedList(2, node)
node3 = LinkedList(1, node2)
node4 = LinkedList(1, node3)


head = node


print(removeDuplicatesFromLinkedList(head).value)

