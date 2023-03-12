# Exercise 1:
# Ask the user for 5 numbers and write them into a list
# a = []
# for i in range(5):
#     b = int(input('Enter 5 digits: '))
#     a.append(b)
# print(a)


# Task 2:
# Given a list A = [1, 2, 3, 4, 5]
# Remove the last number from the list
# a = [1, 2, 3, 4, 5]
# a.pop()
# print(a)


# Task 3:
# Ask the user for 10 numbers and write them to list A
# Ask the user for the number N
# Display to the user how many times the number N is repeated in the list A
# a = []
# for _ in range(10):
#     b = int(input('Enter 10 digits: '))
#     a.append(b)
# print(a)
#
# N = int(input('Enter N number: '))
# print(a.count(N))


# Task 4:
# Ask the user for the number N
# Ask the user for N numbers and write them to list A
# Print the list in reverse order
# a = []
# N = int(input('Enter N number: '))
# for _ in range(1 * N):
#     b = int(input('Enter number: '))
#     a.append(b)
# a.reverse()
# print(a)

# Task 5:
# Ask the user for 5 numbers and write them to list A
# Write all numbers from list A that are greater than 5 to list C
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


# Task 6:
# Ask the user for the number N
# Ask the user for N integers and write them to list A
# Find the minimum and maximum number in it using a loop
# (it is forbidden to use the min, max, sorted, sort function). Output these numbers.
# a = []
# N = int(input('Enter N number: '))
# for _ in range(1 * N):
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


# Task 7:
# The user enters text, you need to display the number of numbers in this text
# Example:
# > 'Lorem 222 ipsum, 123 dolor 1 sit amet
# Number of numbers: 3
# N = str(input('Enter your text: '))
# b = N.split(' ')
# w = []
# for i in b:
#     if i.isdigit():
#         w.append(i)
# print(len(w))
