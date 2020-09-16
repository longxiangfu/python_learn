'''
创建一个数据集，包含1到10的随机整数，总共100个整数。统计每个数字的次数
演练for
'''

import random;

lst = []
for i in range(100):
    n = random.randint(1,10)
    lst.append(n)

dt = {}
for i in lst:
    if i in dt:
        dt[i] +=1
    else:
        dt[i] = 1

print(dt)