def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]

    print(arr)


arr = [9, 8, 6, 4, 3, 1, 2]
bubble_sort(arr)
