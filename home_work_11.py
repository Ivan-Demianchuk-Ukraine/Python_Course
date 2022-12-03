# 1. Написать функцию, которая возвращает слуайную строку заданной длины.
import random


def get_random_string(length: int) -> str:
    c = ''
    for i in range(length):
        letters_or_digits = random.randint(1, 3)
        if letters_or_digits == 1:
            i = random.randint(48, 57)
            c = c + chr(i)
        elif letters_or_digits == 2:
            i = random.randint(65, 90)
            c = c + chr(i)
        elif letters_or_digits == 3:
            i = random.randint(97, 122)
            c = c + chr(i)
    print(c)
    return c


get_random_string(23)
