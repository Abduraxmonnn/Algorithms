def bubble_sort_2(lst):
    index_length = len(lst) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, index_length):
            if lst[i] > lst[i + 1]:
                sorted = False
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

    return lst


print(bubble_sort_2([4, 1, 7, 99, 2, 12, 1, 43, 3]))
