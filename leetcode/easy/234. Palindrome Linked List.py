# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        middle = self.middleNode(head)
        reverse = self.reverseList(middle)

        while reverse:

            if head.val != reverse.val:
                return False
            head = head.next
            reverse = reverse.next

        return True

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head

        while current:
            current.next, prev, current = prev, current, current.next

        return prev
