"""
list 列表
"""
print("---append 向末尾添加元素---")
lst = [1, 2, 3, 4]
lst.append(5)
print(lst) # [1, 2, 3, 4, 5]

print("---insert 在索引处插入元素---")
lst.insert(0, 100)
print(lst) # [100, 1, 2, 3, 4, 5]

print("---extend 添加多个元素---")
lst2 = ['a', 'b']
lst.extend(lst2)
print(lst) # [100, 1, 2, 3, 4, 5, 'a', 'b']
lst.extend('book')
print(lst) # [100, 1, 2, 3, 4, 5, 'a', 'b', 'b', 'o', 'o', 'k']

print("---pop 删除并返回元素---")
print(lst.pop()) # k
print(lst) # [100, 1, 2, 3, 4, 5, 'a', 'b', 'b', 'o', 'o']
print(lst.pop(0)) # 100
print(lst) # [1, 2, 3, 4, 5, 'a', 'b', 'b', 'o', 'o']

print("---remove 删除元素(第一个符合的元素)---")
lst.remove('b')
print(lst) # [1, 2, 3, 4, 5, 'a', 'b', 'o', 'o']

print("---clear 清空列表---")
lst2 = ['a', 'b']
lst2.clear()
print(lst2) # []

print("---sort 排序---")
lst2 = [1, 3, 2, 5]
lst2.sort()
print(lst2) # [1, 2, 3, 5]
lst2.sort(reverse=True)
print(lst2) # [5, 3, 2, 1]
lst2.reverse()
print(lst2) # [1, 2, 3, 5]

print("---str和list互转---")
s = 'python'
lst = list(s)
print(lst) # ['p', 'y', 't', 'h', 'o', 'n']
print(''.join(lst)) # python

