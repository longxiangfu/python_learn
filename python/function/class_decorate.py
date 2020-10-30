"""
类装饰器
"""


class Log:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('I am log')
        self.func()


@Log
def func():
    print('I am a function')


if __name__ == '__main__':
    func()

# I am log
# I am a function
