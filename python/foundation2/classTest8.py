"""
控制属性访问
"""
print("---slot---")
"""
__slots__={'属性a', '属性b'}: 实例只能添加修改指定的属性，不能添加修改额外的属性；类可以添加修改指定的属性和额外的属性
"""
class Foo:
    __slots__ = {'name', 'age'}

f = Foo()
f.name = 'zhangsan'
print(f.name) # zhangsan  实例只能添加指定的属性name和age
# print(f.age) # 报错：AttributeError: 'Foo' object has no attribute 'age'    还没添加age属性，所以报错
# f.sex = 'male' # 报错：AttributeError: 'Foo' object has no attribute 'sex'   添加的属性不在__slots__中，所以报错


class Bar:
    __slots__ = {'name', 'age'}

Bar.name = 'zhangsan'
print(Bar.name) # zhangsan
print(Bar.age) # <member 'age' of 'Bar' objects>
Bar.sex = 'male'
print(Bar.sex) # male


print("---调用实例没有的属性时会报错，可以使用getattr和setattr来解决---")
class A:pass
a = A()
# print(a.name) # 报错：AttributeError: 'A' object has no attribute 'name'

class B:
    def __getattr__(self, name):
        print("you use gerattr")

    def __setattr__(self, name, value):
        print("you use setattr")
        self.__dict__[name] = value

b = B()
print(b.x)
# you use gerattr
# None
b.x = "haha"
print(b.x)
# you use setattr
# haha