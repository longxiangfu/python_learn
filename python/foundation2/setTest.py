"""
set 集合
"""
import copy

print("---定义。无序不可重复---")
s = set([2, 5, 4, 4, 2])
print(s) # {2, 4, 5}
s2 = {'python', 2, 3}
print(s2) # {'python', 2, 3}
print(type(s2)) # <class 'set'>

print("---集合中的需要时不可变对象---")
# {'python', [1,2,3]} # TypeError: unhashable type: 'list'
{'python', (1,2,3)}
['name', 123, ['python', 'php']]
['name', 123, ('python', 'php')]

print("---添加元素---")
print(s) # {2, 4, 5}
s.add('python')
print(s) # {2, 4, 5, 'python'}

print("---删除元素---")
print(s) # {2, 4, 5, 'python'}
s.pop()
print(s) # {4, 5, 'python'}
s.remove(4)
print(s) # {5, 'python'}
s.discard(5)
s.discard(5)
print(s) # {'python'}   discard: 元素存在则删除，不存在则不报错
#s.remove(5) # KeyError: 5    remove: 元素存在则删除，不存在则报错

print("---复制: 同列表和字典的拷贝---")
print('浅拷贝')
b1 = ['name', 123, ['python', 'php']]
b2 = b1.copy()
print(b2) # ['name', 123, ['python', 'php']]
print(b1 is b2) # False
print(b1[2][0]) # python
b1[2][0] = 999
print(b1) # ['name', 123, [999, 'php']]
print(b2) # ['name', 123, [999, 'php']]  因为是浅拷贝，列表对象引用的是同一个对象，所以b1的修改会体现在b2中
b1[0] = 'name1'
print(b1) # ['name1', 123, [999, 'php']]
print(b2) # ['name', 123, [999, 'php']]
b1[1] = 1234
print(b1) # ['name1', 1234, [999, 'php']]
print(b2) # ['name', 123, [999, 'php']]  str和int是值传递，所以是深拷贝

print('深拷贝')
b3 = ['name', 123, ['python', 'php']]
b4 = copy.deepcopy(b3)
print(f"b1 is b2 : {b1 is b2}") # b1 is b2 : False
print(b3[2][0]) # python
b3[2][0] = 999
print(b3) # ['name', 123, [999, 'php']]
print(b4) # ['name', 123, ['python', 'php']]  深拷贝
b3[0] = 'name1'
print(b3) # ['name1', 123, [999, 'php']]
print(b4) # ['name', 123, [999, 'php']]
b3[1] = 1234
print(b3) # ['name1', 1234, [999, 'php']]
print(b4) # ['name', 123, [999, 'php']]  str和int是值传递，所以是深拷贝

print("---集合运算---")
s = set('python')
print(s) # {'n', 'h', 'o', 't', 'p', 'y'}
print('a' in s) # False
print('y' in s) # True
print(f"len is {len(s)}") # len is 6
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
print(a.issuperset(b)) # True   issuperset是否是超集
print(b.issubset(a)) # True   issubset是否是子集
print(a|b) # {1, 2, 3, 4, 5}
print(a.union(b)) # {1, 2, 3, 4, 5}   |或union 并集
print(a&b) # {1, 2, 3}
print(a.intersection(b)) # {1, 2, 3}   &或intersection 交集
print(a-b) # {4, 5}
print(a.difference(b)) # {4, 5}   -或difference 差集



