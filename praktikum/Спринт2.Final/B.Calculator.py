# Лацис Дмитрий Сергеевич
# Задача: B. Калькулятор
# ID: 52887765
# URL: https://contest.yandex.ru/contest/23759/run-report/52887765/


import operator


class Calculator:

    MATH_OPERATORS = {
        '*': operator.mul,
        '-': operator.sub,
        '+': operator.add,
        '/': operator.floordiv
    }

    def __init__(self):

        self.__items = []

    def is_empty(self):
        return len(self.__items) == 0

    def get_operation(self, operation):
        if operation in self.MATH_OPERATORS:
            return self.MATH_OPERATORS[operation]

    def add_memory_value(self, value):
        self.__items.append(value)

    def get_memory_values(self):

        if len(self.__items) > 1:
            return self.__items.pop(), self.__items.pop()

    @staticmethod
    def run_operation(operand_1, operand_2, operation):
        return operation(operand_2, operand_1)

    def get_result(self):
        if not self.is_empty():
            return self.__items.pop()


if __name__ == '__main__':

    calc = Calculator()
    items = input().split()

    for item in items:

        if item.isdigit() or item[1:].isdigit():
            calc.add_memory_value(int(item))
        else:
            operation = calc.get_operation(item)

            if operation:

                first_num, second_num = calc.get_memory_values()

                calc.add_memory_value(
                    int(calc.run_operation(first_num, second_num, operation))
                )

    print(calc.get_result())
