"""
类属性：在java中称作类属性或静态属性
"""
print("---类属性，类可以访问，实例也可以访问---")
class Foo:
    lang = 'python'

print(Foo.lang) # python
f = Foo()
print(f.lang) # python


print("---类修改类属性，实例也自动修改类属性；实例修改类属性，类不会修改类属性---")
Foo.lang = 'java'
print(Foo.lang) # java
print(f.lang) # java
f.lang = 'c++'
print(Foo.lang) # java
print(f.lang) # c++


print("---类添加的属性为类属性，类和实例都可以访问；实例添加的属性为该实例属性，只有该实例才能访问 ---")
Foo.group = 'laoqi'
print(Foo.group) # laoqi
print(f.group) # laoqi
f.age = 18
# print(Foo.age) # AttributeError: type object 'Foo' has no attribute 'age'
print(f.age) # 18

