"""
普通装饰器演示三：计算函数执行时间，更加通用
"""

import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)

    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1


@timethis
def list_append():
    lst = []
    for i in range(1000000):
        lst.append(i)


@timethis
def list_compre():
    [i for i in range(1000000)]


countdown(10000)
countdown(10000000)
list_append()
list_compre()
# countdown 0.000995635986328125
# countdown 0.8118045330047607
# test_list_append 0.18849992752075195
# test_list_compre 0.09075236320495605
