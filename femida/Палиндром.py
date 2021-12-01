# https://femida.yandex-team.ru/problems/434

"""
Написать функцию, которая определяет, является ли переданная строка палиндромом
(читается слева-направо и справа-налево одинаково).

Примеры палиндромов:
- Казак
- А роза упала на лапу Азора
- Do geese see God?
- Madam, I’m Adam

Ограничение по памяти O(1).
"""

def is_palindrome(s):

    start = 0
    end = len(s) - 1

    while start < end:

        start_char = s[start]
        end_char = s[end]

        if not start_char.isalpha():
            start += 1

        if not end_char.isalpha():
            end -= 1

        if start_char.lower() != end_char.lower():
            return False

        start += 1
        end -= 1

    return True

print(is_palindrome('A man, a plan, a canal: Panama'))