"""
列表解析：列表生成表达式
集合解析：集合生成表达式
字典解析：字典生成表达式
生成器解析：生成器生成表达式
"""

# 列表解析
lst = [i for i in range(10)]
print(lst)
print(type(lst))
# 集合解析
s = {i for i in range(10)}
print(s)
print(type(s))


# 字典解析
d = {i: i + 10 for i in range(10)}
print(d)
print(type(d))


# 生成器解析
g = (i for i in range(10))
print(g)
print(type(g))
for i in g:
    print(i)
