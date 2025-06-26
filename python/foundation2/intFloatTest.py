"""
int  float
"""
import decimal
from decimal import Decimal

# 查看类型
print('---查看类型---')
print(type) # <class 'type'>
print(type(2)) # <class 'int'>
print(type(3.14)) # <class 'float'>

# 类型转换
print('---类型转换---')
print(int(3.14)) # 3
print(float(3)) # 3.0
print(int()) # 0
print(str(2.56)) # '2.56'

# 查看内存地址
print('---查看内存地址---')
print(id(3))
print(id(3.0))

# 加减乘除
print('---加减乘除---')
a = Decimal('10')
b = Decimal('3')
print(a + b)
print(a - b)
print(a * b)
print(a / b) # 3.33... 除法
print(a // b) # 3 整除
print(a % b) # 1 取余
print(a ** b) # 1000 幂
print(divmod(a, b)) # (Decimal('3'), Decimal('1'))   商3余1

# 取舍
print('---取舍---')
a = Decimal('1.456')
print(a.quantize(Decimal('0.01'), rounding=decimal.ROUND_HALF_UP)) # 1.46 四舍五入
print(a.quantize(Decimal('0.01'), rounding=decimal.ROUND_DOWN)) # 1.45 向下取整
print(a.quantize(Decimal('0.01'), rounding=decimal.ROUND_UP)) # 1.46 向上取整

print('---help---')
help(help(id))