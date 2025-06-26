"""
迭代器
"""
import itertools

print("---可迭代对象(能被循环)：有iter方法的对象---")
print(hasattr(list, '__iter__')) # True
print(hasattr(iter([]), '__iter__')) # True


print("---迭代器：不仅有iter方法，还有next方法---")
lst = [1, 2, 3]
iter_lst = iter(lst)
print(hasattr(iter_lst, '__next__')) # True
print(iter_lst.__next__()) # 1
print(iter_lst.__next__()) # 2
print(iter_lst.__next__()) # 3
# print(iter_lst.__next__()) # 报错 StopIteration

iter_lst2 = iter(lst)
for i in iter_lst2:
    print(i)
# 1
# 2
# 3


print("---利用工具生成迭代器---")
counter = itertools.count(start=5, step=1)
print(type(counter)) # <class 'itertools.count'>
print(counter.__next__()) # 5
print(counter.__next__()) # 6
print(counter.__next__()) # 7