from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        new_node = ListNode(0)
        dummy = new_node
        extra = 0

        while l1 or l2:

            num = extra

            if l1:
                num += l1.val
                l1 = l1.next

            if l2:
                num += l2.val
                l2 = l2.next

            dummy.next = ListNode(num % 10)
            dummy = dummy.next
            extra = num // 10

        if extra > 0:
            dummy.next = ListNode(extra)

        return new_node.next


node2 = ListNode(3)
node1 = ListNode(4, node2)
node = ListNode(2, node1)

root2 = ListNode(4)
root1 = ListNode(6, root2)
root = ListNode(5, root1)

head = Solution().addTwoNumbers(node, root)

while head:

    print(head.val)
    head = head.next

