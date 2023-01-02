# Задание 1
# Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers.
# чтобы выполнился код, нужно скачать у меня с репозитория либо создать файл с именем test.txt

# f = open('test.txt', 'r')
# items = f.read().split()
# numbers = []
# for i in items:
#     if i.isdigit():
#         numbers.append(i)
#     else:
#         pass
# print(numbers)
# f.close()

# Задание 2
# Запросить у пользователя текст и записать его в файл data.txt
# text = str(input('Enter Text: '))
# my_file = open('data.txt', 'w+')
# my_file.write(text)
# my_file.close()

# Задание 3
# Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл numbers.txt через пробел
# a = []
# N = int(input('Enter Number: '))
# f = open('numbers.txt', 'w+')
# for i in range(N * 1):
#     b = int(input('Enter Number: '))
#     f.write(str(b) + ' ')
# f.close()

#
# Задание 4
# Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число
# import random
# f = open('random_numbers.txt', 'w+')
# for i in range(100):
#     b = random.randint(1, 8)
#     f.write(str(b) + '\n')
# f.close()


# Задание 5
# Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю
# чтобы выполнился код, нужно скачать у меня с репозитория либо создать файл с именем test.txt

# f = open('test.txt', 'r')
# a = f.read().split()
# only_words = []
# for i in a:
#     if i.isalpha():
#         only_words.append(i)
#     elif '\n' in i:
#         only_words.append(i)
#     else:
#         pass
# print(len(only_words))
# f.close()

#
# Задание 6
# Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел

# f = open('numbers.txt', 'w+')
# f.write('1 2 4 5 6 7 8 9 10')
# f.close()

# f = open('numbers.txt', 'r')
# numbers = f.read().split()
# numbers = [int(i) for i in numbers]
# print(sum(numbers))
# f.close()

# Задание 7
# чтобы выполнился код, нужно скачать у меня с репозитория либо создать файл с именем BigText.txt
# Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
# 'в' - 20 раз
# 'привет' - 10 раз
# 'как' - 9 раз
# 'у' - 7
# 'world' -

# file = open('BigText.txt', 'r')
# items = file.read().split()
# dicts = {}
# for i in items:
#     if i not in dicts:
#         dicts[i] = 0
#     elif i in dicts:
#         dicts[i] += 1
# j = sorted(dicts.items(), key=lambda y: y[1], reverse=True)
# print(j)
# print(j[0])
# print(j[1])
# print(j[2])
# print(j[3])
# print(j[4])
# file.close()
