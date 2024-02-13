def find_maximum(arr):
    maximum = arr[0]

    for i in arr:
        if maximum < i:
            maximum = i

    return maximum


arr = [1, 2, 4, 5, 7]
print(find_maximum(arr))