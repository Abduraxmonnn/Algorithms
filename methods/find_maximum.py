def find_maximum(arr):
    maximum = arr[0]

    for item in arr:
        if item > maximum:
            maximum = item

    return maximum


arr = [1, 2, 4, 5, 7]
print(find_maximum(arr))
