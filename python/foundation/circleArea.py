"""
输入半径，计算圆的面积
"""

import math
import decimal

r = float(input("请输入半径:"))
decimalR = decimal.Decimal(str(math.pi))
area = decimalR * decimal.Decimal(r) * decimal.Decimal(r)
print("area类型：", type(area))
print("圆的面积：", round(area, 2))
