class Array(object):
    def __init__(self, size, defaultValue=None):
        self.size = size
        if defaultValue is None:
            self.items = list()
            for i in range(size):
                self.items.append(defaultValue)
        else:
            self.items = list()

            if len(defaultValue) == size or len(defaultValue) < size:
                for j in range(len(defaultValue)):
                    if defaultValue[j] or defaultValue[j] == 0:
                        self.items.append(defaultValue[j])
                for i in range(len(defaultValue), size):
                    self.items.append(None)
            else:
                print('Elements are more than the size specified')

    def myLen(self):
        length = 0
        for i in self.items:
            if i is None:
                continue
            else:
                length += 1
        return length

    def insertFirst(self, element):
        if self.myLen() < self.size:
            for i in range(self.myLen(), 0, -1):
                self.items[i] = self.items[i - 1]
            self.items[0] = element
        else:
            print('Element index out of range 1')

    def insertAtIndex(self, index, element):
        if self.myLen() < self.size:
            for i in range(self.myLen(), index, -1):
                self.items[i] = self.items[i - 1]
            self.items[index] = element
        else:
            print('Element index out of range 2')

    def insertAfterIndex(self, index, element):
        if self.myLen() < self.size:
            for i in range(self.myLen(), index + 1, -1):
                self.items[i] = self.items[i - 1]
            self.items[index + 1] = element
        else:
            print('Element index out of range 3')

    def insertAfterElement(self, element):
        if self.myLen() < self.size:
            for i in range(self.myLen()):
                if self.items[i] == element:
                    self.insertAfterIndex(i, element)
        else:
            print('Element index out of range 4')
# insertBeforeIndex

    def delete(self, element):
        if element in self.items:
            Index = self.items.index(element)
            self.items[Index] = None
        else:
            print('This element is not in the Array!')

    def deleteElement(self, element):
        if element in self.items:
            Index = self.items.index(element)
            self.items[Index] = None
        else:
            print('This element is not in the Array!')

    def search(self, element):
        if element in self.items:
            position = 0
            for i in range(self.myLen()):
                if self.items[i] == element:
                    break
                else:
                    position += 1

            print('Element {} found at position {}'.format(element, position))
        else:
            print('This element is not in the Array!')

    def countElement(self, element):
        if element in self.items:
            count = 0
            for i in range(self.myLen()):
                if self.items[i] == element:
                    count += 1
            print('Element "{}" found {} times'.format(element, count))
        else:
            print('This element was not found in the list')

    def deleteFirstElement(self, is_ood_or_even):
        if self.myLen() <= self.size:
            if is_ood_or_even == 1 or is_ood_or_even == 0:
                if is_ood_or_even == 0:
                    for i in range(self.myLen()):
                        print("---> ", self.items[i])
                        if self.items[i] % 2 == 0:
                            self.items[i] = None
                            break
                else:
                    for j in range(self.myLen()):
                        if self.items[j] % 2 == 1:
                            self.items[j] = None
                            break
            else:
                print('deleteFirstElement() takes {} positional arguments but waited 0 (Even number) or 1 (Odd number)'.format(is_ood_or_even))
        else:
            print('Element index out of range 5')


if __name__ == '__main__':
    myArray = Array(5, [99, 5, 0, 1, 0])
    print(myArray.items, myArray.myLen())
    myArray.insertFirst(3)
    print(myArray.items, myArray.myLen())
    myArray.insertAfterIndex(1, 4)
    print(myArray.items, myArray.myLen())
    myArray.delete(5)
    print(myArray.items, myArray.myLen())
    myArray.search(4)

    myArray.insertAfterElement(99)
    myArray.deleteElement(99)
    myArray.countElement(1)
    print(myArray.items, myArray.myLen())
