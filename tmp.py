# class Parent:
#     def add(self, a, b):
#         print(f"{a + b} This is a method from Parent")
#
#     def append(self, a, b):
#         print(f"{a + b} This is a append method from Parent")
#
#     def add1(self, a, b):
#         return f"{a * b} This is a method from Parent"
#
#
# class Parent1(Parent):
#     # def add(self, a, b):
#     #     print(f"This is a method from Parent1")
#
#     def method1(self, a, b):
#         print(f"This is a method from Parent1")
#
#
# class Parent2(Parent):
#     def add(self, a, b):
#         # result = super().add(a, b)  # Return NoneType coz parent class method is not return anything
#         result = super().add1(a, b)  # Return calculated value coz parent class method return calculated value
#         print(f"{result} This is a method from Parent2")
#
#
# class MyClass(Parent1, Parent2):
#     pass
#
#
# obj = MyClass()
# obj.method1(10, 10)
# obj.add(5, 5)
# obj.append(50, 10)


# def my_generator(n):
#     for i in range(n + 1):
#         yield i
#
#
# my_gen = my_generator(5)
#
# for i in my_gen:
#     print(i)


# Определяем генератор
def my_generator():
    yield "Hello World"
    yield [1, 2, 3, 4, 5]
    yield 3
    yield 4
    yield 5


# Получаем итератор из генератора
my_iterator = my_generator()

# Выводим элементы итератора
print(next(my_iterator))  # выведет "Hello World"
print(next(my_iterator))  # выведет [1, 2, 3, 4, 5]
print(next(my_iterator))  # выведет 3
# print(next(my_iterator))  # выведет 4
# print(next(my_iterator))  # выведет 5
