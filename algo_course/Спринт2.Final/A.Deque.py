# Лацис Дмитрий Сергеевич
# Задача: A. Дек
# ID: 52887754
# URL: https://contest.yandex.ru/contest/23759/run-report/52887754/


class Deque:

    def __init__(self, max_size):

        self.max_size = max_size
        self.__items = [None] * self.max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_out_of_memory(self):
        return self.size == self.max_size

    def push_front(self, value):

        if self.is_out_of_memory():
            return -1

        if self.size < self.max_size:

            if self.__items[self.head] is not None:
                self.head = (self.head - 1) % self.max_size

            self.__items[self.head] = value
            self.size += 1

    def push_back(self, value):

        if self.is_out_of_memory():
            return -1

        if self.size < self.max_size:

            if self.__items[self.tail] is not None:
                self.tail = (self.tail + 1) % self.max_size

            self.__items[self.tail] = value
            self.size += 1

    def pop_front(self):

        if self.is_empty():
            return -1

        tmp = self.__items[self.head]
        self.__items[self.head] = None
        self.head = (self.head + 1) % self.max_size

        self.size -= 1

        if self.is_empty():
            self.head = 0
            self.tail = 0

        return tmp

    def pop_back(self):

        if self.is_empty():
            return -1

        tmp = self.__items[self.tail]
        self.__items[self.tail] = None
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1

        if self.is_empty():
            self.head = 0
            self.tail = 0

        return tmp


if __name__ == '__main__':

    commands_length = int(input())
    deque = Deque(int(input()))

    for _ in range(commands_length):

        method, *argument = input().split()

        value = getattr(deque, method)(*argument)

        if value == -1:
            print('error')
        elif value is not None:
            print(value)
