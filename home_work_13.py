def custom_zip(*lists, full=False, default=None) -> list:
    all_lists, result_list = [], []
    for i in lists:
        all_lists.append(len(i))
    min_list, max_list = min(all_lists), max(all_lists)

    if full == True:
        for i in lists:
            if max_list > len(i):
                while max_list > len(i):
                    i.append(default)
        print(*lists)

    else:
        count = 0
        timely_list = []
        for _ in range(min_list):
            for i, value in enumerate(lists):
                timely_list.append(value[count])
            count += 1

        for i in range(min_list):
            index = 0
            p = []
            for _ in range(len(lists)):
                p.append(timely_list[index])
                index += 1
                if len(p) == (len(lists)):
                    result_list.append(tuple(p))
                    for _ in range(len(lists)):
                        timely_list.pop(0)
        return result_list


print(custom_zip([1, 2, 3, 4, 5], [9, 8, 7]))
