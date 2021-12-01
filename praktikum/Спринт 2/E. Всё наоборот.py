def solution(node):

    prev = None
    current = node

    while current:

        current.next, current.prev, current, prev = prev, current, current.next, current

    return prev
