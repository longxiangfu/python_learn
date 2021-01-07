# -!- coding: utf-8 -!-
"""
演示张量
"""
import numpy as np

"""
定义二阶张量
"""
z = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
"""
定义三阶张量
"""
n_z = np.array([z, z*2, z*3])

print(n_z)
print(type(n_z))
print(n_z.ndim)  # 阶数
print(n_z.shape)  # 形状
print(n_z.dtype)  # 数据类型

# [[[ 1  2  3]
#   [ 4  5  6]
#   [ 7  8  9]]
#
#  [[ 2  4  6]
#   [ 8 10 12]
#   [14 16 18]]
#
#  [[ 3  6  9]
#   [12 15 18]
#   [21 24 27]]]
# <class 'numpy.ndarray'>
# 3
# (3, 3, 3)
# int32