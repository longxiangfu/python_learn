"""
封装：优点鸡肋
在属性或方法前加两个下划线__，表示属性或方法是私有的
"""
class Foo:
    __name = 'zhangsan'
    def __init__(self):
        self.__group = 'lisi'
    def __author(self):
        return '__author'

    @staticmethod
    def __show():
        return '__show'

f = Foo() # f.时看不到属性name、属性group、方法author、方法show, 但是可以通过特殊的方法访问到
print(dir(f)) # ['_Foo__author', '_Foo__group', '_Foo__name', '_Foo__show',。。。]
print(dir(Foo)) # ['_Foo__author', '_Foo__group', '_Foo__name', '_Foo__show',。。。]
print(f._Foo__name) # zhangsan
print(f._Foo__group) # lisi
print(f._Foo__show()) # __show
print(f._Foo__author()) # __author

