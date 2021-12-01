# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        even = head.next
        odd = head

        while odd.next:
            ...



obj4 = ListNode(4)
obj3 = ListNode(3)
obj1 = ListNode(2)
obj = ListNode(1)

head = Solution().oddEvenList(obj)

while head:

    print(head.val)
    head = head.next