from typing import Callable, Iterable


def custom_map(func: Callable, *iterables) -> Iterable:
    result_list = []
    values_amount = len(iterables)
    if hasattr(func, '__builtins__'):
        length_min_list = []
        for x in iterables:
            length_min_list.append(len(x))
        length_min = min(length_min_list)
        for j in range(0, length_min):
            temp_list = []
            i = 0
            while i < len(iterables):
                temp_list.append(iterables[i][j])
                i = i + 1
            temp_list = tuple(temp_list)
            result_list.append(func(*temp_list))
    else:
        if values_amount == 1 and len(iterables[0]) > 1:
            result_list = [func(iterables[0][i]) for i in range(0, len(iterables[0]))]

    return result_list


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
