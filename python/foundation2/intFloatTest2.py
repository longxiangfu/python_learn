"""
int  float
"""
import math
from decimal import Decimal

print('---取舍---')
a = Decimal('0.12')
b = Decimal('0.29')
print(a + b) # 0.41 正常
print(round(a + b, 1)) # 0.4 四舍五入保持小数点后一位
print((a+b).quantize(Decimal('0.1'), rounding='ROUND_HALF_UP')) # 0.4 四舍五入保持小数点后一位
print((a+b).quantize(Decimal('0.1'), rounding='ROUND_DOWN')) # 0.4 向下取整保持小数点后一位
print((a+b).quantize(Decimal('0.1'), rounding='ROUND_UP')) # 0.5 向上取整保持小数点后一位

print('---math函数---')
print(math.pi) # 3.141592653589793  pi
print(math.pow(2, 3)) # 8.0 幂
print(Decimal('2')**Decimal('3')) # 8 幂