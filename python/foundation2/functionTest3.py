"""
特殊函数
"""
print("---lambda表达式: 是个函数---")
"""
lambda parameters: expression

def <lambda>(parameters):
    return expression
"""
def add(x):
    return x + 3
print(add(2)) # 5

lam = lambda x: x + 3
print(type(lam)) # <class 'function'>
print(lam(2)) # 5


print("---map函数: 对列表中的元素进行操作---")
"""
map(function, *iterables): 将迭代器中每个元素都应用到函数上
"""
m = map(lambda x: x+3, range(3))
print(type(m)) # <class 'map'>
print(list(m)) # [3, 4, 5]

m1 = map(lambda x,y,z:x+y+z, range(3), range(3), range(3))
print(list(m1)) # [0, 3, 6]


print("---filter函数: 对列表中的元素进行过滤---")
"""
filter(function, iterable): 将迭代器中每个元素应用到函数上，返回function表达式为真的元素
"""
f = filter(lambda x: x>0, range(-3,3))
print(type(f)) # <class 'filter'>
print(list(f)) # [1, 2]

print([i for i in range(-3, 3) if i > 0]) # [1, 2]


