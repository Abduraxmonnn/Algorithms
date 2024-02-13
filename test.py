def chkPerfectSquare(n):
    i = 1
    while i * i <= n:
        if (n % i == 0) and (n / i == i):
            return i
        i = i + 1
    return False


# Driver code
if __name__ == "__main__":
    num = int(input("Enter the Number: "))
    if (chkPerfectSquare(num)):
        print(num, "is a perfect square.")
    else:
        print(num, "is not a perfect square.")
