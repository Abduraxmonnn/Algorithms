class Solution(object):
    def deleteDuplicates(self, head):
        new_list = []

        for element in head:
            if element not in new_list:
                new_list.append(element)
        return new_list


if __name__ == '__main__':
    head = [1, 1, 2, 3, 3]
    print(Solution().deleteDuplicates(head))
