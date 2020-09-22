'''
假设有字典数据：d={'c':39, 'b':40, 'c':99},字典的键值对还可以增加，
编写函数，实现对这个字典中键值对的查询。
例如提供如a=1, b=40等参数，查询这些是否为此数据的值
'''

def findkv(dct, **kwargs):
    r = {k:v for k, v in kwargs.items() if dct.get(k) == v}
    return r

d={'c':39, 'b':40, 'c':99}
fr = findkv(d, a=1, b=40)
print(fr)