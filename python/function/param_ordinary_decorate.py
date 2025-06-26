"""
带参数的装饰器
"""


def log(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == 'info':
                print('this is a info log')
            elif level == 'error':
                print('this is a error log')
            res = func(*args, **kwargs)
            return res

        return wrapper

    return decorator


@log(level='error')
def fun1():
    print('I am a function1')


@log(level='info')
def fun2():
    print('I am a function2')


fun1()
# this is a error log
# I am a function1
fun2()
# this is a info log
# I am a function2
