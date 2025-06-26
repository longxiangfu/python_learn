"""
条件语句
"""
import random

print("---if---")
a = 5
if a > 3:
    a += 1
print(a)

s = 'python'
if 'p' in s:
    s = 'you need ' + s
print(s)

print("---random  随机数---")
print(random.randint(1, 10))
print(random.randint(1, 10))

print("---三元操作，类似java中三目操作---")
x = 2
a = 'python' if x > 2 else 'java'
print(a)

print("---if else---")
a = 1
if a == 5:
    print("a is 5")
elif a == 4:
    print("a is 4")
elif a == 3:
    print("a is 3")
elif a == 2:
    print("a is 2")
elif a == 1:
    print("a is 1")
else:
    print("a is else num")

