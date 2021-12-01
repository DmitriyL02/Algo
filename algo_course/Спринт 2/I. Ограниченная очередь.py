class MyQueueSized:

    def __init__(self, max_size):

        self.max_size = max_size
        self.items = [None] * max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        if self.size < self.max_size:
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1

    def pop(self):
        if self.is_empty():
            return

        position_value = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1

        return position_value

    def peek(self):
        if self.is_empty():
            return
        return self.items[self.head]

    def queue_size(self):
        return self.size


if __name__ == '__main__':

    commands_counter = int(input())
    queue = MyQueueSized(int(input()))

    for _ in range(commands_counter):

        command = input().split()

        if command[0] == 'peek':
            print(queue.peek())
        elif command[0] == 'push':
            if queue.queue_size() == queue.max_size:
                print('error')
            else:
                queue.push(command[1])
        elif command[0] == 'size':
            print(queue.queue_size())
        elif command[0] == 'pop':
            print(queue.pop())


