

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

def my_function(s: str):
    print(f'memory address INSIDE BEFORE func,  s = {id(s)}')
    s += "new letters"
    print(f'memory address INSIDE AFTER func,   s = {id(s)}')

s = "abc"
print(f'memory address BEFORE calling func, s = {id(s)}')
my_function(s)
print(f'memory address AFTER calling func, s = {id(s)}')
print(f'{s=}')
