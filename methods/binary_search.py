# # Iterative
# def binary_search(array, x):
#     low = 0
#     high = len(array) - 1
#
#     while low <= high:
#
#         mid = low + (high - low) // 2
#
#         if array[mid] == x:
#             return array[mid]
#         elif array[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#
#     return -1
#
#
# array = [3, 4, 5, 6, 7, 8, 9]
# x = 4
#
# result = binary_search(array, x)
# print(result)

# # Recursive
def binary_search(array, low, high, x):
    while low <= high:

        mid = (high + low) // 2

        if array[mid] == x:
            return array[mid]
        elif array[mid] < x:
            return binary_search(array, mid + 1, high, x)
        else:
            return binary_search(array, low, mid - 1, x)


    return -1

array = [3, 4, 5, 6, 7, 8, 9]
x = 10
result = binary_search(array,0, len(array) - 1, x)
print(result)
