"""
dict 字典
"""

print("---定义---")
d = {'name':'longxiangfu', 'age':29}
print(d) # {'name': 'longxiangfu', 'age': 29}
print(dict(a=1, b=2, c=3)) # {'a': 1, 'b': 2, 'c': 3}

print("---key不可重复，并且必须是不可变对象---")
#dict(a=1, b=2, c=3, a=2) #key重复了
{(1,2,3):'hello'} # 正常
#{[1,2,3]:'hello']} #key必须是不可变对象

print("---操作---")
print(d['name']) # longxiangfu
print(d['age']) # 29
del d['name']
print(d) # {'age': 29}
print('age' in d) # True
print('name' in d) # False