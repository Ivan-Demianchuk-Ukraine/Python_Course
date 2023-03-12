def custom_map(function, *iterables):
    result = []
    min_length = min(len(iterable) for iterable in iterables)
    for i in range(min_length):
        args = [iterable[i] for iterable in iterables]
        result.append(function(*args))
    return result


sum2 = lambda x, y: x + y
sum3 = lambda x, y, z: x + y + z
assert custom_map(sum, [[1, 2, 3], [4, 5]]) == [6, 9]
assert custom_map(len, [[], (2, 4), [1, 3, 5, 7]]) == [0, 2, 4]
assert custom_map(str, (17, 23)) == ['17', '23']
assert custom_map(sum2, [1, 2, 3], [3, 5, 0]) == [4, 7, 3]
assert custom_map(sum2, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44)) == [4, 6, 7, 8]
assert custom_map(sum3, [1, 1, 1], [4, 5], [0, 5, 2, 1]) == [5, 11]
assert custom_map(min, [[1, 2, 3], [4, 5]]) == [1, 4]
assert custom_map(max, [[1, 2, 3], [4, 5]]) == [3, 5]
print(custom_map(min, [[757, 0, 4, 6], [8, 5, 6, 7], [2, 3, 356], [1, 88, 555], [123, 55]]))  # [0, 5, 2, 1, 55]
sum4 = lambda x, y, z, t: x + y + z + t
print(custom_map(sum4, [1, 2, 3, 4], [2, 3, 4, 5], [0, 0, 0, 0, 0, 0, 1, 0], [4, 5, 1, 2]))


def sum2def(x, y):
    return x, y


print(custom_map(sum2def, [1, 2, 3], [3, 5, 0]))


map