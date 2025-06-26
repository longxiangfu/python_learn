'''
普通装饰器演示二：计算函数执行时间
'''

import time


def timing_fun(func):
    def wrapper():
        start = time.time()
        func()
        stop = time.time()
        return stop - start

    return wrapper


@timing_fun
def test_list_append():
    lst = []
    for i in range(1000000):
        lst.append(i)


@timing_fun
def test_list_compre():
    [i for i in range(1000000)]


a = test_list_append()
b = test_list_compre()
print(a)
print(b)
# 0.14760565757751465
# 0.08477449417114258
