# Дан текст T и строка S. Требуется найти подстроку S' в T такую,
# что она совпадает с S с точностью до перестановки букв.

def substring(text, s):

    letters = dict()

    for letter in text:
        letters[letter] = letters.get(letter, 0) + 1

    

substring('abcdefghtyot', 'ght')

