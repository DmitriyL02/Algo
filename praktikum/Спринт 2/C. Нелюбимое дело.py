# C. Нелюбимое дело.py
# Comment it before submitting
# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item


def solution(node, idx):

    counter = 0

    head = node

    if idx == 0:
        head = node.next_item
        return head

    while node.next_item:
        if counter + 1 == idx:
            node.next_item = node.next_item.next_item
            return head
        node = node.next_item

        counter += 1

    return head
