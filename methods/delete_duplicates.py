class Solution(object):
    def deleteDuplicates(self, head):
        new_l = []

        for element in head:
            if element not in new_l:
                new_l.append(element)
        return new_l


if __name__ == '__main__':
    head = [1, 1, 2, 3, 3]
    print(Solution().deleteDuplicates(head))
