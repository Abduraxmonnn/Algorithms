def gradingStudents(grades):
    # Write your code here

    result = []

    for i in range(0, len(grades)):
        if grades[i] < 5:
            continue
        elif grades[i] < 38:
            result.append(grades[i])
        elif grades[i] % 5 >= 3:
            value = grades[i]
            divided = grades[i] % 5
            res = (5 - divided) + value
            result.append(res)
        else:
            result.append(grades[i])

    print(result)


if __name__ == '__main__':
    grades = [4, 73, 67, 38, 33]
    gradingStudents(grades)

#
#
# https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
