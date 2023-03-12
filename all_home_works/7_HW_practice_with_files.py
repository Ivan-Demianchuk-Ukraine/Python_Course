# Exercise 1
# Given a file with arbitrary text, you need to find all the numbers in the file and write it to the numbers list.
# to run the code, you need to download from my repository or create a file called test.txt

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

# Task 2
# Ask the user for text and write it to the data.txt file

# text = str(input('Enter Text: '))
# my_file = open('data.txt', 'w+')
# my_file.write(text)
# my_file.close()

# Task 3
# Ask the user for the number N and ask for N numbers from the user, then write them to the numbers.txt file separated
# by a space

# a = []
# N = int(input('Enter Number: '))
# f = open('numbers.txt', 'w+')
# for i in range(N * 1):
#     b = int(input('Enter Number: '))
#     f.write(str(b) + ' ')
# f.close()

# Task 4
# Generate 100 random numbers and write them to the random_numbers.txt file, where one line = one number

# import random
# f = open('random_numbers.txt', 'w+')
# for i in range(100):
#     b = random.randint(1, 8)
#     f.write(str(b) + '\n')
# f.close()


# Task 5
# Given a file with arbitrary text, you need to find the number of words in the file and display to the user
# to run the code, you need to download from my repository or create a file called test.txt

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


# Task 6
# Given a file that contains numbers separated by a space, you need to display the sum of these numbers to the user

# f = open('numbers.txt', 'w+')
# f.write('1 2 4 5 6 7 8 9 10')
# f.close()

# f = open('numbers.txt', 'r')
# numbers = f.read().split()
# numbers = [int(i) for i in numbers]
# print(sum(numbers))
# f.close()


# Task 7
# to execute the code, you need to download from my repository or create a file named BigText.txt
# Given a file in which the text is written, it is necessary to display the top 5 lines that are most often repeated,
# for example:
# 'в' - 20 times
# 'привет' - 10 times
# 'как' - 9 times
# 'у' - 7 - times
# 'world' - times

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
