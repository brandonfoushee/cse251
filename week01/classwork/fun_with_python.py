

# x = 1
# print(f'memory address x = {id(x)}')
# x = 2
# print(f'memory address x = {id(x)}')

# d = {}
# d["1"] = "1"
# print(f'memory address d = {id(d)}')
# d["2"] = "2"
# print(f'memory address d = {id(d)}')

# l = []
# print(f'memory address l = {id(l)}')
# l.append("1")
# print(f'memory address l = {id(l)}')
# l.append("2")
# print(f'memory address l = {id(l)}')

# def func(x: int):
#     print(f'memory address INSIDE BEFORE func,  x = {id(x)}')
#     x = 2
#     print(f'memory address INSIDE AFTER func,   x = {id(x)}')

# x = 1
# print(f'memory address BEFORE calling func, x = {id(x)}')
# func(x)
# print(f'memory address AFTER calling func,  x = {id(x)}')
# print(f'{x=}')

# def my_function(s: str):
#     print(f'memory address INSIDE BEFORE func,  s = {id(s)}')
#     s += "new letters"
#     print(f'memory address INSIDE AFTER func,   s = {id(s)}')

# s = "abc"
# print(f'memory address BEFORE calling func, s = {id(s)}')
# my_function(s)
# print(f'memory address AFTER calling func, s = {id(s)}')
# print(f'{s=}')

# my_list = []
# my_list.append(1)
# my_tuple = (1, 2, 3)

class Animal():   
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        
    def print_attribute(self):
        print(f'{self.name=}')
        print(f'{self.age=}')
        
#person1 = Animal("Roger", 30)
#person1.print_attribute()

class Dog(Animal):
    def __init__(self, name: str, age: int, color: str) -> None:
        super().__init__(name, age)
        self.color = color

dog1 = Dog("Fido", 10, "brown")
dog1.print_attribute()