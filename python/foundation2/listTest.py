"""
list 列表
"""

print("---list定义---")
lst = []
print(lst) # []
lst = ['a', 'b', 'c', 'd'] # ['a', 'b', 'c', 'd']
print(lst)
print(list()) # []
print(str()) # ''
print(int()) # 0
print(float()) # 0.0

print("---有序可重复---")
a_lst = ['b', 'a', 'c', 'b']
a_lst.append('d')
print(a_lst) # ['b', 'a', 'c', 'b', 'd']

print("---运算---")
b_lst = [1, 2, 3, 4]
print(a_lst + b_lst) # ['b', 'a', 'c', 'b', 'd', 1, 2, 3, 4]
print(b_lst * 2) # [1, 2, 3, 4, 1, 2, 3, 4]
print(len(b_lst)) # 4
print(1 in b_lst) # True
b_lst.append(5)
print(b_lst) # [1, 2, 3, 4, 5]  增
b_lst[0] = 100
print(b_lst) # [100, 2, 3, 4, 5]  改
print(b_lst[0]) # 100  查
b_lst.remove(4)
print(b_lst) # [100, 2, 3, 5] 删
del b_lst[0]
print(b_lst) # [2, 3, 5] 删
list.clear(b_lst)
print(b_lst) # [] 清空
