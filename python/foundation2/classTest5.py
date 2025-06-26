"""
继承
"""
print("---继承---")
class P:
    lang = 'python'
    def __init__(self, name):
        self.name = name

    def eat(self):
        return 'fish'

    @staticmethod
    def show():
        return 'show'


class C(P):
    pass # 空类


c = C('laoqi')
print(c.lang) # python
print(c.name) # laoqi
print(c.eat()) # fish
print(c.show()) # show


print("---方法重写---")
class E(P):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name) # 调用父类的初始化方法

    def eat(self):
        return 'meat'


e = E('laoqi', 29)
print(e.eat()) # meat
print(e.name) # laoqi

