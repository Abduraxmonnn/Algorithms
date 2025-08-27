class Node:
    def __init__(self, data):
        self.Data = data

    Data = None
    Next = None


class LStack:
    head = None
    count = 0

    def isEmpty(self):
        return self.count == 0

    def counter(self):
        return self.count

    def push(self, item):
        node = Node(item)
        node.Next = self.head
        self.head = node
        self.count += 1

    def pop(self):
        if self.isEmpty():
            print("Stek bo\'sh")
            return None
        temp = self.head
        self.head = self.head.Next
        self.count -= 1
        return temp.Data

    def peek(self):
        if self.isEmpty():
            print("Stek bo\'sh")
            return None
        return self.head.Data

    def clear(self):
        self.head = None
        self.count = 0

    def contains(self, data):
        current = self.head
        while current is not None:
            if current.Data is data:
                return True
            current = current.Next
        return False

    def print(self):
        current = self.head
        while current is not None:
            print(current.Data)
            current = current.Next

    def deleteFirstElement(self):
        current = self.head
        if self.isEmpty():
            print('Stack bo\'sh')
        new_s = []
        for i in range(0, self.count - 1):
            pass


class Main:
    def main(*args):
        stack = LStack()
        stack.push(8)
        stack.push(16)
        stack.push(32)
        stack.push(64)
        stack.push(4)
        stack.pop()
        stack.print()
        print()
        header = stack.peek()
        print("Stek uchi: ", header)
        print()
        stack.deleteFirstElement()


if __name__ == "__main__":
    Main.main([])
