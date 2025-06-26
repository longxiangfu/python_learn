"""
__str__:对用户友好，即print(实例)打印出的内容就是该方法中定义的内容
__repr__：对解释器友好，即在命令窗口中直接输入实例，输出的内容就是该方法中定义的内容
"""
class Foo:
    def __str__(self):
        return 'I am in str'

    def __repr__(self):
        return 'I am in repr'


f = Foo()
print(f)


