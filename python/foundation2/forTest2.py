"""
循环语句for
"""
print("---range 产生一定范围的数---")
r = range(4)
print(r) # range(0, 4)
print(type(r)) # <class 'range'>
for i in r:
    print(i)
# 0
# 1
# 2
# 3

print("---range转list---")
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("---获取20以内能被3整除的数---")
lst = []
for i in range(20):
    if i % 3 == 0:
        lst.append(i)
print(lst) # [0, 3, 6, 9, 12, 15, 18]
print(list(range(0, 20, 3))) # [0, 3, 6, 9, 12, 15, 18]

print("---zip---")
a = 'python'
b = 'qiwsir'
z = zip(a, b)
print(z) # <zip object at 0x000001EF2473FBC0>
print(type(z)) # <class 'zip'>
print(list(z)) # [('p', 'q'), ('y', 'i'), ('t', 'w'), ('h', 's'), ('o', 'i'), ('n', 'r')]
c = [1, 2, 3]
d = [4, 5, 6, 7]
print(list(zip(c,d))) # [(1, 4), (2, 5), (3, 6)]    长度不一样，以短的为准

print("---将两个可迭代对象对应的数字相加，放到list中去---")
c = [1, 2, 3, 4, 5]
d = [5, 6, 7, 8, 9]
lst = []
for i in range(len(c)):
    lst.append(c[i] + d[i])
print(lst) # [6, 8, 10, 12, 14]
lst.clear()
for i, j in zip(c, d):
    lst.append(i + j)
print(lst) # [6, 8, 10, 12, 14]
lst.clear()
lst = [i+j for i, j in zip(c, d)]
print(lst) # [6, 8, 10, 12, 14]  列表解析


print("---列表解析：让python更接近自然语言---")
print([i * 2 for i in range(10)]) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print([i for i in range(10) if i % 2 == 0]) # [0, 2, 4, 6, 8]