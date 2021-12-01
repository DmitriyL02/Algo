# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if not head:
            return False

        low = fast = head

        while fast.next and fast.next.next:

            low = low.next
            fast = fast.next.next

            if low == fast:
                return True

        return False
