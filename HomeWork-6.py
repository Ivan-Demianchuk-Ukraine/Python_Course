# Задание 1:
# Запросить у пользователя 5 чисел и записать их в список
# a = []
# for i in range(5):
#     b = int(input('Enter 5 digits: '))
#     a.append(b)
# print(a)


# Задание 2:
# Дан список A = [1, 2, 3, 4, 5]
# Удалить последнее число из списка
# a = [1, 2, 3, 4, 5]
# a.pop()
# print(a)


# Задание 3:
# Запросить у пользователя 10 чисел и записать их в список A
# Запросить у пользователя число N
# Вывести пользователю сколько в списке A повторяется число N
# a = []
# for _ in range(10):
#     b = int(input('Enter 10 digits: '))
#     a.append(b)
# print(a)
#
# N = int(input('Enter N number: '))
# print(a.count(N))


# Задание 4:
# Запросить у пользователя число N
# Запросить у пользователя N чисел и записать их в список A
# Вывести список в обратной последовательности
# a = []
# N = int(input('Enter N number: '))
# for _ in range(1*N):
#     b = int(input('Enter number: '))
#     a.append(b)
# a.reverse()
# print(a)

# Задание 5:
# Запросить у пользователя 5 чисел и записать их в список A
# Записать все числа из списка A которые больше 5 в список C
# a = []
# c = []
# for _ in range(5):
#     b = int(input('Enter number: '))
#     a.append(b)
#     if b > 5:
#         c.append(b)
#     else:
#         pass
# print(c)

# Задание 6:
# Запросить у пользователя число N
# Запросить у пользователя N целых чисел и записать их в список A
# Найти в нем минимальное и максимальное число с помощью цикла
# (запрещено использовать функцию min, max, sorted, sort). Вывести эти числа.

# a = []
# N = int(input('Enter N number: '))
# for _ in range(1*N):
#     b = int(input('Enter WHOLE number: '))
#     a.append(b)

# maximum = a[0]
# minimum = a[0]
# for i in a:
#     if maximum < i:
#         maximum = i
#     if minimum > i:
#         minimum = i
# print(maximum)
# print(minimum)

# Задание 7:
# Пользователь вводит текст нужно вывести количество чисел в этом тексте
# Пример:
# > 'Lorem 222 ipsum, 123 dolor 1 sit amet
# Количество чисел: 3
# N = str(input('Enter your text: '))
# b = N.split(' ')
# w = []
# for i in b:
#     if i.isdigit():
#         w.append(i)
# print(len(w))
