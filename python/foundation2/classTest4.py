"""
方法
"""
print("---实例方法：同java的实例方法---")
class Foo():
    def method(self, x):
        return x*2

f = Foo()
print(f.method(2)) # 4
# print(Foo.method(2)) # 报错   类无法调用实例方法


print("---静态方法：同java的静态方法---")
class Bar:
    @staticmethod
    def add():
        return 'add'

print(Bar.add()) # add
f = Bar()
print(f.add()) # add


