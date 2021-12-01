class LinkedList:

    def __init__(self, value, next=None):

        self.value = value
        self.next = next


class Queue:

    def __init__(self):

        self.head = None
        self.tail = None
        self.queue_size = 0

    def get(self):

        if not self.is_empty():
            item = self.head

            if self.head == self.tail:
                self.head = self.tail = None
            elif self.head.next:
                self.head = self.head.next
            else:
                self.head = None

            self.queue_size -= 1
            return item.value
        return

    def put(self, item):

        if self.head is None and self.tail is None:
            self.head = self.tail = LinkedList(item)
        else:
            self.tail.next = LinkedList(item)
            self.tail = self.tail.next

        self.queue_size += 1

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.size() == 0


if __name__ == '__main__':

    queue = Queue()

    for _ in range(int(input())):

        command = input().split()

        if command[0] == 'put':
            queue.put(command[1])
        elif command[0] == 'get':
            if queue.is_empty():
                print('error')
            else:
                print(queue.get())
        elif command[0] == 'size':
            print(queue.size())
