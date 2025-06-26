"""
实例属性：同java的实例属性
"""
print("---实例属性可以在实例化时指定，也可以是默认值---")
class Bar:
    def __init__(self, name):
        self.name = name # self.name中的name为实例属性    等号右面的name为形参
        self.age = 18 # self.age中的age为实例属性，为默认值

a = Bar('zhangsan')
print(a.name) # zhangsan
b = Bar('lisi')
print(b.name) # lisi


print("---dict：列出实例的所有实例属性和值---")
print(a.__dict__) # {'name': 'zhangsan', 'age': 18}


print("---self指向当前的实例对象---")
class Foo():
    def __init__(self):
        print(self)
f = Foo() # <__main__.Foo object at 0x000001C7CBDE2B40>
print(f) # <__main__.Foo object at 0x000001C7CBDE2B40>

