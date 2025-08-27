def birthdayCakeCandles(candles):
    count = 0
    largest_number = candles[0]

    for number in candles:
        if number > largest_number:
            largest_number = number
    for i in candles:
        if i == largest_number:
            count += 1

    print(count)  # return count


if __name__ == '__main__':
    c = [1, 2, 1, 3]
    birthdayCakeCandles(c)
