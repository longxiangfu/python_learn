"""
str
"""
import sys

print('---获取系统默认编码方式---')
print(sys.getdefaultencoding()) # utf-8

print('---str基本定义---')
a = 'hello world'
print(type(a)) # <class 'str'>

print('---str和int互转---')
print(int('123')) # 123
print(str(123)) # '123'

print('---特殊字符转义---')
print('what \'s your name?')