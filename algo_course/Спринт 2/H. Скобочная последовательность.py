class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_last(self):
        if not self.is_empty():
            return self.items[-1]


def is_correct_bracket_seq(sequence):

    if not sequence:
        return True

    stack = Stack()

    for bracket in sequence:

        if bracket == '(':
            stack.push(')')
        elif bracket == '[':
            stack.push(']')
        elif bracket == '{':
            stack.push('}')
        elif stack.get_last() == bracket:
            stack.pop()
        else:
            return False
    if stack.is_empty():
        return True
    return False


if __name__ == '__main__':

    seq = list(input())

    print(is_correct_bracket_seq(seq))
