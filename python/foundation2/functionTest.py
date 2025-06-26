"""
函数
"""
print("---函数定义---")
def add(x, y):
    return x + y

print(add(1, 2)) # 3
print(add('abc', 'de')) # abcde    按照参数位置调用(位置参数)


print("---函数调用：按照参数名称调用（关键字参数）---")
def foo(x, y):
    print('x=', x)
    print('y=', y)

foo(x=1, y=2) # x= 1  y= 2
foo(y=1, x=2) # x= 2  y= 1


print("---函数没有返回值时，返回的是None---")
print(foo(1, 2)) # None


print("---函数参数默认值：带默认值的参数要放在最后---")
def bar(x, y=3, z=4):
    print('x=', x)
    print('y=', y)
    print('z=', z)

bar(1, 2, 3)
# x= 1
# y= 2
# z= 3
bar(1)
# x= 1
# y= 3
# z= 4


print("---函数可以返回多个值---")
def my_fun():
    return 1,2,3

r = my_fun()
print(r) # (1, 2, 3)
print(type(r)) # <class 'tuple'>
a,b,c = my_fun()
print(a,b,c) # 1 2 3


print("---函数参数*args：必须是位置参数；收集为元组---")
def fun(x, *args):
    print('x=', x)
    print('args=', args)
    print('type(args)=', type(args))
fun(1, 2, 3, 4)
# x= 1
# args= (2, 3, 4)
# type(args)= <class 'tuple'>
fun(1)
# x= 1
# args= ()
# type(args)= <class 'tuple'>


print("---函数参数**kwargs：必须是关键字参数；收集为字典---")
def bar(x, **kwargs):
    print('x=', x)
    print('kwargs=', kwargs)
    print('type(kwargs)=', type(kwargs))

bar(1, a=2, b=3)
# x= 1
# kwargs= {'a': 2, 'b': 3}
# type(kwargs)= <class 'dict'>


print("---函数参数*args和**kwargs---")
def foo(*args, **kwargs):
    print(args)
    print(kwargs)
foo(1,2,a=3,b=4)
# (1, 2)
# {'a': 3, 'b': 4}
