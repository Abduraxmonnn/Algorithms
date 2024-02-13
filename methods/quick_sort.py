def quick_sort(arr):
    length = len(arr)

    if length <= 1:
        return arr
    else:
        middle = arr.pop()

    items_greater = []
    items_lower = []

    for i in arr:
        if i > middle:
            items_greater.append(i)
        else:
            items_lower.append(i)

    return quick_sort(items_lower) + [middle] + quick_sort(items_greater)


print(quick_sort([5, 2, 4, 12, 8, 6]))
