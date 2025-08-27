def plusMinus(arr):
    # Write your code here
    zero = 0
    negative = 0
    positive = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            negative += 1
        elif arr[i] > 0:
            positive += 1
        else:
            zero += 1

    print('%0.6f' % (positive / len(arr)))
    print('%0.6f' % (negative / len(arr)))
    print('%0.6f' % (zero / len(arr)))


if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]
    # arr = [1, 2, 3, -1, -2, -3, 0, 0]
    print(plusMinus(arr))
