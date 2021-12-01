class Stack:

    def __init__(self):
        self.items = []
        self.max_value = []

    def push(self, item):
        if not self.max_value or self.max_value[-1] <= item:
            self.max_value.append(item)
        self.items.append(item)

    def pop(self):
        if self.max_value and self.max_value[-1] == self.items[-1]:
            self.max_value.pop()
        self.items.pop()

    def get_max(self):
        if self.max_value:
            return self.max_value[-1]


if __name__ == '__main__':

    stack = Stack()

    for _ in range(int(input())):

        command = input().split()

        if command[0] == 'get_max':
            print(stack.get_max())
        elif command[0] == 'pop':
            if stack.items:
                stack.pop()
            else:
                print('error')
        elif command[0] == 'push':
            stack.push(int(command[1]))