'''
随机生成一个10以内的整数，若该数大于圆周率，则当作直径计算圆的周长和面积，否则
当作半径计算圆的周长和面积，并将计算结果输出
演示if
'''

import random
import math

n = random.randint(1, 10)
if n > math.pi:
    perimeter = math.pi * n
    area = math.pi * (n/2) ** 2
else:
    perimeter = math.pi * n * 2
    area = math.pi * pow(n, 2)

print("n:", n)
print("perimeter:", perimeter)
print("area:", area)