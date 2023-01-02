#Написать декоратор, который будет принимать в качестве параметра file_name, считать количество вызовов функций и записывать в файл в формате f'{func_name} была вызвана {count} раза.\n'
#
# Пример:
# @call_times('foo.txt')
# def foo():
#   pass
#
# @call_times('foo.txt')
# def boo():
#   pass
#
# @call_times('calls.txt')
# def doo():
#   pass
#
# foo()
# boo()
# foo()
# foo()
# boo()
# doo()

# Файл foo.txt:
# foo была вызвана 3 раза
# boo была вызвана 2 раза
#
# Файл calls.txt:
# doo была вызвана 1 раза
import time
#
#
# def call_times(file_name):
#     c = open(file_name, 'r')
#     return c.readline()
#
# start = time.time()
# func()
# end = time.time()
# print(end - start)

# print(call_times('BigText.txt'))


# @call_times('BigText.txt')
# def test():

# for i in range(100000):
#     pass
# def test():
#     pass
#
#
# def call_times(file_name, function):
#     f = open(file_name, 'w')
#     c = f.writelines('asdf')
#     return function
#
#
# @call_times('calls.txt', test())

# count_test = 0
# count_pex = 0
#
#
# def decor(f, file_name):
#     f()
#     open_file = open(file_name, 'w')
#     global count_pex
#     global count_test
#     if file_name == 'foo.txt':
#         count_pex += 1
#         open_file.writelines(f'{f.__name__} was called {count_pex} times')
#     elif file_name == 'calls.txt':
#         count_test += 1
#         open_file.writelines(f'{f.__name__} was called {count_test} times')
#
#
# def test():
#     for i in range(100000):
#         pass
#
#
# def pex():
#     for i in range(1000000):
#         pass
#
#
# def dex():
#     for i in range(10000000):
#         pass
#
#
# print(decor(pex, 'calls.txt'))
# print(decor(pex, 'foo.txt'))
# print(decor(test, 'calls.txt'))
# print(decor(pex, 'foo.txt'))
# print(decor(test, 'calls.txt'))
# print(decor(pex, 'foo.txt'))
# print(decor(test, 'calls.txt'))


# count_test = 0
# count_pex = 0
#
#
# def decor(f, file_name):
#     f()
#     open_file = open(file_name, 'w')
#     global count_pex
#     global count_test
#     if file_name == 'foo.txt':
#         count_pex += 1
#         open_file.writelines(f'{f.__name__} was called {count_pex} times')
#     elif file_name == 'calls.txt':
#         count_test += 1
#         open_file.writelines(f'{f.__name__} was called {count_test} times')
#
#
# def test():
#     for i in range(100000):
#         pass
#
#
# def pex():
#     for i in range(1000000):
#         pass
#
#
# def dex():
#     for i in range(10000000):
#         pass
#
#
# print(decor(pex, 'calls.txt'))
# print(decor(pex, 'foo.txt'))
# print(decor(test, 'calls.txt'))
# print(decor(pex, 'foo.txt'))
# print(decor(test, 'calls.txt'))
# print(decor(pex, 'foo.txt'))
# print(decor(test, 'calls.txt'))




#
# i = 0
# def global_decorator(file_name):
#     def internal_decorator(func):
#         def inner():
#             func()
#             f = open(file_name, 'w')
#             global i
#             i += 1
#             f.writelines(f'{func.__name__} was called {str(i)} times')
#         return inner
#     return internal_decorator
#
#
# @global_decorator('calls.txt')
# def test():
#     print('middle')
#
# @global_decorator('foo.txt')
# def pex():
#     print('middle')
#
#
#
# test()
# test()
# pex()
# pex()












# def global_decorator(file_name):
#     def internal_decorator(func):
#         def inner():
#             func()
#             f = open(file_name, 'r')
#             c = f.readlines()
#             g = str(c).split()
#             if g[0] == func.__name__:
#                 f2 = open(file_name, 'w')
#                 f2.writelines(f'{func.__name__} was called {str(int(g[3]) + 1)} times')
#             elif g[0] != func.__name__:
#                 f2 = open(file_name, 'w')
#                 f2.writelines(f'{func.__name__} was called {str(int(g[3]) + 1)} times')
#
#                     # f.close()
#
#                     # print(f2)
#         return inner
#     return internal_decorator
#
#
# @global_decorator('calls.txt')
# def test():
#     pass
#
# @global_decorator('foo.txt')
# def pex():
#     pass
#
# @global_decorator('foo.txt')
# def rex():
#     pass
#
#
# test()
# test()
# pex()
# test()
# pex()
# test()
# rex()


def global_decorator(file_name):
    def internal_decor(func):
        def inner():
            print('asd')
            open_read = open(file_name, 'r')
            content_in_massive = open_read.readlines()
            print(content_in_massive)
            for i in content_in_massive:
                if func.__name__ in i:
                    idx = content_in_massive.index(i)
                    print('already exist')
                    m = int(i[0])
                    new_number = str(m + 1)
                    n = i.replace(i[0], new_number)
                    content_in_massive[idx] = n
                    o = open(file_name, 'w').writelines(content_in_massive)
                else:
                     print('oooo', content_in_massive)
                     content_in_massive.append(f'1 time was called {func.__name__}')
                     print('plp',content_in_massive)
                     o = open(file_name, 'a').writelines(content_in_massive)
            func()
            print('fgh')
        return inner
    return internal_decor

@global_decorator('calls.txt')
def test():
    print('test-ops')

@global_decorator('foo.txt')
def pex():
    print('pex-ops')



pex()
pex()
test()
pex()
test()
pex()


# a = open('foo.txt', 'r')
# b = a.readlines()
# for i in b:
#     if '1' in i or '2' in i:
#         print(i)
#         print('YES')
#     elif '1' or '2' not in i:
#         print('NO')
#     else:
#         print('fuck')
#
# content_in_massive = ['asd', 'qwe']
#
# content_in_massive[0] = 'SSS'
# print(content_in_massive)


