import copy


def custom_zip(*lists, full=False, default=None) -> list:
    copy_lists = copy.deepcopy(lists)
    copy_lists_len = len(copy_lists)
    all_lists_lens, result_list = [], []
    for i in copy_lists:
        all_lists_lens.append(len(i))
    min_list, max_list = min(all_lists_lens), max(all_lists_lens)

    if full:
        for i in copy_lists:
            while max_list > len(i):
                i.append(default)
        all_lists_lens = []
        for i in copy_lists:
            all_lists_lens.append(len(i))
        min_list, max_list = min(all_lists_lens), max(all_lists_lens)
        count = 0
        timely_list = []
        for _ in range(min_list):
            for i, value in enumerate(copy_lists):
                timely_list.append(value[count])
            count += 1

        for i in range(min_list):
            index = 0
            two_items_list = []
            for _ in range(copy_lists_len):
                two_items_list.append(timely_list[index])
                index += 1
                if len(two_items_list) == copy_lists_len:
                    result_list.append(tuple(two_items_list))
                    for _ in range(copy_lists_len):
                        timely_list.pop(0)
        return result_list

    else:
        count = 0
        timely_list = []
        for _ in range(min_list):
            for i, value in enumerate(copy_lists):
                timely_list.append(value[count])
            count += 1

        for i in range(min_list):
            index = 0
            two_items_list = []
            for _ in range(copy_lists_len):
                two_items_list.append(timely_list[index])
                index += 1
                if len(two_items_list) == copy_lists_len:
                    result_list.append(tuple(two_items_list))
                    for _ in range(copy_lists_len):
                        timely_list.pop(0)
        return result_list

# autotests


seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
seq3 = [9, 8, 7]
print(custom_zip(seq1, seq2, seq3, full=True, default="Q"))
print('ww', seq1, seq2, seq3)
print(list(zip(seq1, seq2, seq3)))
print(custom_zip(seq1, seq2, seq3))
print(list(zip(seq1, seq2, seq3)))
print(custom_zip([1, 2, 3, 4, 5], [9, 8, 7], [9, 8, 7]))
print(list(zip([1, 2, 3, 4, 5], [9, 8, 7], [9, 8, 7])))
print(custom_zip([1, 2, 3, 4, 5], [9, 8, 7], full=True, default='Q'))
a, b = [2, 2, 3, 4, 5], [9, 8, 7]
print(custom_zip(a, full=True, default='Q'))
print(custom_zip(b, a, full=True, default='Q'))
