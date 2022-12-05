def custom_map(function, *lists) -> list:
    result_all_lists, result_one_list = [], []
    for one_list in list(zip(*lists)):
        for item in one_list:
            result_one_list.append(item)
            if len(result_one_list) == len(one_list):
                result_one_list = function(result_one_list)
                result_all_lists.append(result_one_list)
                result_one_list = []
    return result_all_lists


print(custom_map(min, [757, 0, 4, 6], [8, 5, 6, 7], [2, 3, 356], [1, 88, 555], [123, 55]))
