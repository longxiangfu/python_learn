"""
tuple：不可变对象，不能修改；是序列，有index方法
list: 可变对象；是序列，有index方法
"""
print("---定义---")
t = (1, 2, "python", [1, 2, 3])
print(t) # (1, 2, 'python', [1, 2, 3])
print(type(t)) # <class 'tuple'>

print("---有index方法，但是不能修改，是不可变对象---")
print(t.index(2)) # 1
#t[1] = 200 # TypeError: 'tuple' object does not support item assignment

print("---tuple和list互转---")
lst = list(t)
print(lst) # [1, 2, 'python', [1, 2, 3]]
lst[1] = 200
t = tuple(lst)
print(t) # (1, 200, 'python', [1, 2, 3])