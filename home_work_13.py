def custom_zip(*lists, full=False, default=None) -> list:
    lists_len = len(lists)
    all_lists_lens, result_list = [], []
    for i in lists:
        all_lists_lens.append(len(i))
    min_list, max_list = min(all_lists_lens), max(all_lists_lens)

    if full:
        for i in lists:
            while max_list > len(i):
                i.append(default)
        all_lists_lens = []
        for i in lists:
            all_lists_lens.append(len(i))
        min_list, max_list = min(all_lists_lens), max(all_lists_lens)

        count = 0
        timely_list = []
        for _ in range(min_list):
            for i, value in enumerate(lists):
                timely_list.append(value[count])
            count += 1

        for i in range(min_list):
            index = 0
            two_items_list = []
            for _ in range(lists_len):
                two_items_list.append(timely_list[index])
                index += 1
                if len(two_items_list) == (lists_len):
                    result_list.append(tuple(two_items_list))
                    for _ in range(lists_len):
                        timely_list.pop(0)
        return result_list

    else:
        count = 0
        timely_list = []
        for _ in range(min_list):
            for i, value in enumerate(lists):
                timely_list.append(value[count])
            count += 1

        for i in range(min_list):
            index = 0
            two_items_list = []
            for _ in range(lists_len):
                two_items_list.append(timely_list[index])
                index += 1
                if len(two_items_list) == (lists_len):
                    result_list.append(tuple(two_items_list))
                    for _ in range(lists_len):
                        timely_list.pop(0)
        return result_list


print(custom_zip([1, 2, 3, 4, 5], [9, 8, 7], full=True, default='Q'))
