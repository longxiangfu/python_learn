'''
计算重力 G = mg, g = 9.8
要求，定义g和使用函数进行计算分别是两种权限
'''

def weight(g):
    def cal_mg(m):
        return m * g
    return cal_mg

w = weight(10)
G = w(100)
print(G)

w2 = weight(9.8)
G2 = w2(100)
print(G2)