def find_minimum(arr):
    minimum = arr[0]

    for i in range(0, len(arr)):
        if minimum > arr[i]:
            minimum = arr[i]

    return minimum


arr = [1, 2, 4, 5, 7]
print(find_minimum(arr))
