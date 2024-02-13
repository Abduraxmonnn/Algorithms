class Solution2(object):
    def Task2(self, list1):
        new_list = []

        while list1:
            minimum = list1[0]
            for x in list1:
                if x < minimum:
                    minimum = x
            new_list.append(minimum)
            list1.remove(minimum)

        return new_list


if __name__ == '__main__':
    list1 = [5, 2, 4, 12, 3, 54, 16, 7]
    print(Solution2().Task2(list1))
