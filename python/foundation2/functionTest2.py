"""
函数
"""
print("---函数也是对象。foo：函数对象   foo()：调用函数---")
def bar():
    print('I am bar')

def foo(f):
    f()

foo(bar) # I am bar    这里的bar表示bar函数对象    foo()表示调用foo函数
print(foo) # <function foo at 0x000002DAAB595BC0>
print(bar) # <function bar at 0x000002DAAB35A2A0>


def opt_seq(func, seq):
    r = [func(i) for i in seq]
    return r

print(opt_seq(abs, range(-2, 2))) # [2, 1, 0, 1]
print(opt_seq(str, range(1, 3))) # ['1', '2']


print("---函数嵌套---")
def foo():
    def bar():
        print('I am bar')
    return bar

a = foo()
print(a) # <function foo.<locals>.bar at 0x000001CA50E95BC0>
a() # I am bar
foo()() # I am bar


print("---函数作用域---")
print("---局部作用域（局部变量）---")
def my_function():
    x = 10 # 局部变量
    print(x) # 10
my_function()

print("---全局作用域（全局变量）---")
y = 20 # 全局变量
def show_y():
    print(y) # 20  可以访问全局变量
show_y()

count = 0 # 全局变量
def increment():
    global count
    count += 1 # 修改全局变量，必须使用global关键字申明
increment()
print(count) # 1

print("---嵌套作用域（子函数修改父函数的局部变量）---")
def outer():
    a = 10 # 父函数的局部变量
    def inner():
        nonlocal a
        a = 20 # 修改父函数的局部变量,必须使用nonlocal关键字申明
    inner()
    print(a) # 20
outer()

