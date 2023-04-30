def miniMaxSum(arr):
    # SORTING LIST
    for i in range(0, len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # CALCULATING SUM
    get_min = arr[0:len(arr) - 1]
    min_sum = 0

    for i in range(len(get_min)): min_sum += get_min[i]

    get_max = arr[1:len(arr)]
    max_sum = 0

    for i in range(len(get_max)): max_sum += get_max[i]

    print(min_sum, max_sum)


if __name__ == '__main__':
    arr = [7, 69, 2, 221, 8974]
    print(miniMaxSum(arr))

# SECOND WAY
# print(sum(arr[0:len(arr) - 1]), sum(arr[1:len(arr)]))
