"""
类的基本定义
"""
class Foo:
    def __init__(self): # 初始化方法，类实例化时调用
        print('I am in init')
        self.x = 'python'  # x为实例属性
f = Foo() # I am in init    类实例化，默认调用init方法
print(f.x) # python     获取实例属性