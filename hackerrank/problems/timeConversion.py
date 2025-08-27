def timeConversion(s):
    if s[-2:] == 'AM' and s[:2] == '12':
        return '00' + s[2:-2]
    elif s[-2:] == 'PM' and s[:2] == '12':
        return '12' + s[2:-2]
    elif s[-2:] == 'PM':
        return str(int(s[:2]) + 12) + s[2:-2]
    else:
        return s[:-2]


if __name__ == '__main__':
    s = '07:05:45PM'
    print(timeConversion(s))
