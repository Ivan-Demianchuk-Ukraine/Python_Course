# Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.
# def change_list(a: list) -> list:
#     try:
#         if a[0] and a[1] in a:
#             a[0], a[-1] = a[-1], a[0]
#             return a
#     except IndexError:
#         print('add more elements in your list')
#
#
# print(change_list([2, 3, 5]))

# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
#  в котором каждый элемент списка является и ключом и значением. Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.


# def to_dict(a: list) -> dict:
#     c = {}
#     for i in a:
#         c[i] = i
#     return c
#
#
# print(to_dict(['as', 'qwe']))


# Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
#  Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.


# def sum_range(a: int, b: int) -> int:
#     if a < b:
#         return sum([i for i in range(a, b + 1)])
#     elif a > b:
#         a, b = b, a
#         return sum([i for i in range(a, b + 1)])
#
#
# print(sum_range(3, 5))


# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить
# на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).

# def read_file(lines: int, file: str):
#     if isinstance(lines, int) and lines > 0:
#         items_list = open(file, 'r').readlines()[:-lines - 1:-1]
#         for i in items_list:
#             print(i.replace('\n', ''))
#
#
# read_file(5, 'test.txt')
