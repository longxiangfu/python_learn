"""
bool
"""
import copy

print("---bool四则运算---")
print(type(False)) # <class 'bool'>
print(type(True)) # <class 'bool'>
print(True+1) # 2
print(True+True) # 2
print(False+1) # 1
print(False+3) # 3
print(True*2) # 2
print(True/2) # 0.5
print(bool(1)) # True
print(bool(0)) # False
print(bool()) # False
print(bool('')) # False
print(bool(' ')) # True
print(bool([])) # False
print(bool(list())) # False
print(bool(tuple())) # False
print(bool(dict())) # False
print(bool(set())) # False

print("---空值---")
print(list()) # []
print(tuple()) # ()
print(dict()) # {}
print(set()) # set()

print("==  !=  >=  <=  <   >")
# ==值是否相等   is引用的是否是同一个对象
"""
字符串、整数、元组：不可变对象；有常量池。注意整数时大时不指向常量池
"""
a = 'hello word'
b = 'hello word'
print(a == b) # True
print(a is b) # True  字符串常量池
"""
列表、字典：可变对象
"""
lst_a = [1,2]
lst_b = [1,2]
print(lst_a == lst_b) # True
print(lst_a is lst_b) # False
lst_c = lst_a.copy()
print(lst_a == lst_c) # True
print(lst_a is lst_c) # False
lst_d = copy.deepcopy(lst_a)
print(lst_a == lst_d) # True
print(lst_a is lst_d) # False