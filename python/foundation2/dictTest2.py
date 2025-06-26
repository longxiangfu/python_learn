"""
dict 字典   是可变对象；不是序列，无index方法
list  可变对象；是序列，有index方法
"""
print("---字典的另一种定义方式---")
d = dict({('a',1), ('lang','python')})
print(d) # {'a': 1, 'lang': 'python'}

print("---字典获取---")
print(d['a']) # 1
#print(d['b']) # KeyError: 'b'
print(d.get('a')) # 1
print(d.get('b')) # None
print(d.get('a', 'laoqi')) # 1  存在key就返回value,否则返回指定值
print(d.get('b', 'laoqi')) # laoqi
d.setdefault('a')
print(d) # {'a': 1, 'lang': 'python'} key有value，不会添加
d.setdefault('b')
print(d) # {'lang': 'python', 'a': 1, 'b': None}  key没有value,添加value为None
d.setdefault('b', 'laoqi')
print(d) # {'a': 1, 'lang': 'python', 'b': None}  key有value，不会添加
d.setdefault('c', 'laoqi')
print(d) # {'lang': 'python', 'a': 1, 'b': None, 'c': 'laoqi'} key没有value,添加设置值

print("---字典添加---")
d.update({('price',3.14), ('color','white')})
print(d) # {'a': 1, 'lang': 'python', 'b': None, 'c': 'laoqi', 'price': 3.14, 'color': 'white'}
d1 = {'city':'handan'}
d.update(d1)
print(d) # {'lang': 'python', 'a': 1, 'b': None, 'c': 'laoqi', 'price': 3.14, 'color': 'white', 'city': 'handan'}

print("---字典删除---")
print(d.pop('lang')) # python
print(d) # {'a': 1, 'b': None, 'c': 'laoqi', 'price': 3.14, 'color': 'white', 'city': 'handan'}
#d.pop('lang') # KeyError: 'lang'
print(d.pop('lang', 'pascal')) # pascal  key没有value,则返回设置值
print(d) # {'a': 1, 'b': None, 'c': 'laoqi', 'price': 3.14, 'color': 'white', 'city': 'handan'}
print(d.popitem()) # ('city', 'handan')   末尾删除
print(d) # {'a': 1, 'b': None, 'c': 'laoqi', 'price': 3.14, 'color': 'white'}