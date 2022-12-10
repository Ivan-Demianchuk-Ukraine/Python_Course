def custom_map(function, *lists) -> list:
    result_list = []
    if '<lambda>' in str(function) and len(lists) == 3:
        if len(lists[0]) == len(lists[1]) and len(lists[1]) == len(lists[2]):
            f, t, n, x, y, h = 0, 1, 2, 0, 0, 0
            for _ in range(len(lists[0])):
                value_from_one, value_from_second, value_from_third = lists[f], lists[t], lists[n]
                result_list.append(function(value_from_one[x], value_from_second[y], value_from_third[h]))
                x, y, h = x + 1, y + 1, h + 1
            return result_list
        elif len(lists[0]) != len(lists[1]) or len(lists[1]) != len(lists[2]):
            o = zip(*lists)
            z = list(o)
            f, t, n, x, y, h = 0, 1, 2, 0, 0, 0
            for _ in range(len(z)):
                value_from_one, value_from_second, value_from_third = lists[f], lists[t], lists[n]
                result_list.append(function(value_from_one[x], value_from_second[y], value_from_third[h]))
                x += 1
                y += 1
                h += 1
            return result_list
    elif '<lambda>' in str(function) and len(lists) == 2:
        if len(lists[0]) == len(lists[1]):
            f, t, x, y = 0, 1, 0, 0
            for _ in range(len(lists[0])):
                value_from_one, value_from_second = lists[f], lists[t]
                result_list.append(function(value_from_one[x], value_from_second[y]))
                x += 1
                y += 1
            return result_list
        elif len(lists[0]) != len(lists[1]):
            o = zip(*lists)
            z = list(o)
            f, t, x, y = 0, 1, 0, 0
            for _ in range(len(z)):
                value_from_one, value_from_second = lists[f], lists[t]
                result_list.append(function(value_from_one[x], value_from_second[y]))
                x += 1
                y += 1
            return result_list
    else:
        result = []
        for i, value in enumerate(*lists):
            result.append(function(value))
        return result


sum2 = lambda x, y: x + y
sum3 = lambda x, y, z: x + y + z
assert custom_map(sum, [[1, 2, 3], [4, 5]]) == [6, 9]
assert custom_map(len, [[], (2, 4), [1, 3, 5, 7]]) == [0, 2, 4]
assert custom_map(str, (17, 23)) == ['17', '23']
assert custom_map(sum2, [1, 2, 3], [3, 5, 0]) == [4, 7, 3]
assert custom_map(sum2, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44)) == [4, 6, 7, 8]
assert custom_map(sum3, [1, 1, 1], [4, 5], [0, 5, 2, 1]) == [5, 11]
