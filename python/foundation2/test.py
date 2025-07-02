"""
map类
map(func, *iterables) --> map object
迭代器中每个元素都应用函数func,返回map类的对象
"""
# mp = map(int, [2,3])
# print(type(map)) # <class 'map'>
# print(dir(mp))
# for i in mp:
#     print(i)
# # 2
# # 3
#
#
# a,b = map(int, [2,3])
# print(a,b)
# # 2 3


"""
返回'add'对应的字典中的value,赋值给str
"""
str = {'add':'add_f', 'multiply':'multiply_f'}['add']
print(str) # add_f