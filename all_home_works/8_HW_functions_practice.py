# Write a change(lst) function that takes a list and swaps its first and last element.
# Initial list has at least 2 elements.
def change_list(a: list) -> list:
    try:
        if a[0] and a[1] in a:
            a[0], a[-1] = a[-1], a[0]
            return a
    except IndexError:
        print('add more elements in your list')


print(change_list([2, 3, 5]))

# Write a to_dict(lst) function that takes a list argument and returns a dictionary,
# where each element of the list is both a key and a value. It is assumed that the elements of the list will comply
# with the rules for specifying keys in dictionaries.


def to_dict(a: list) -> dict:
    c = {}
    for i in a:
        c[i] = i
    return c


print(to_dict(['as', 'qwe']))


# Write a function sum_range(start, end) that sums all integers from "start" to "end" inclusive.
# If the user specifies the first number is greater than the second, just swap them.

def sum_range(a: int, b: int) -> int:
    if a < b:
        return sum([i for i in range(a, b + 1)])
    elif a > b:
        a, b = b, a
        return sum([i for i in range(a, b + 1)])


print(sum_range(3, 5))


# Write a read_last(lines, file) function that will open a specific file file and output
# to print line by line the last lines in the number of lines (just in case, check that a positive integer is given).

def read_file(lines: int, file: str):
    if isinstance(lines, int) and lines > 0:
        items_list = open(file, 'r').readlines()[:-lines - 1:-1]
        for i in items_list:
            print(i.replace('\n', ''))


# read_file(5, 'test.txt')
