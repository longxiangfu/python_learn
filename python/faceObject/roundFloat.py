"""
类特殊方法，内部调用了内置函数
"""


class RoundFloat:
    def __init__(self, value, value1):
        self.value = value
        self.value1 = value1

    def __str__(self):  # 对用户友好 repr 对解释器友好
        return "{0:.2f}".format(self.value)

    __repr__ = __str__


r = RoundFloat(3.1415926, 4.5669)
print(r)
print(type(r))
