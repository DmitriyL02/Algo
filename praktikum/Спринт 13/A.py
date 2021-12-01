def find_max_value_finder(node, max_value):

    if not node:
        return max_value

    if node.value > max_value:
        max_value = node.value

    return max(find_max_value_finder(node.left, max_value), find_max_value_finder(node.right, max_value))


def solution(node):
    return find_max_value_finder(node, node.value)
