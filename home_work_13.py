def custom_zip(*lists) -> list:
    result_list = []
    shortest_list_is = []
    for i in lists:
        shortest_list_is.append(len(i))
    shortest_list_is = min(shortest_list_is)

    count = 0
    timely_list = []
    for _ in range(shortest_list_is):
        for i, value in enumerate(lists):
            timely_list.append(value[count])
        count += 1
    print(count, timely_list)

    for i in range(shortest_list_is):
        m = 0
        p = []
        for _ in range(len(lists)):
            p.append(timely_list[m])
            m += 1
            if len(p) == (len(lists)):
                print("yes")
                result_list.append(tuple(p))
                p = []
                m = 0
                for _ in range(len(lists)):
                    timely_list.pop(0)
        print('q', timely_list)
        print('w', result_list)


    # for i in
    return result_list


print(custom_zip([1, 2, 3, 4, 5], [9, 8, 7]))
