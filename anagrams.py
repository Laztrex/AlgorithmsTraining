# Даны две строки, состоящие из строчных латинских букв. Требуется определить, являются ли эти строки анаграммами,
# т. е. отличаются ли они только порядком следования символов.
#
# Формат ввода Входной файл содержит две строки строчных латинских символов, каждая не длиннее 100 000 символов.
# Строки разделяются символом перевода строки.
#
# Формат вывода
# Выходной файл должен содержать единицу, если строки являются анаграммами, и ноль в противном случае.
#
# Пример 1
# Ввод	Вывод
# qiu     1
# iuq
#
# Пример 2
# Ввод	Вывод
# zprl    0
# zprc

import sys


def anagram(word_1, word_2):
    for letter in word_1:
        if letter in word_2:
            word_2.remove(letter)
            continue
        else:
            return 0
    else:
        return 1 if len(word_2) == 0 else 0


print(anagram(sys.stdin.readline().strip(), list(sys.stdin.readline().strip())))

