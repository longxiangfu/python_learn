"""
pandas绘制数据,需依赖matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel("E:\\pycharmWork\\python\\auto\\people.xlsx")
students.sort_values(by='Score', inplace=True, ascending=False)
print(students)

# x轴按strdents.name的长度进行均分
x = range(len(students.Name))
plt.xticks(x, students.Name)
# 定义x轴和y轴
plt.bar(x, students.Score, color='orange')

# 定义标题、x轴标签和y轴标签
plt.title('Students', fontsize=16)
plt.xlabel('name')
plt.ylabel('score')

# 将x轴内容旋转90度
plt.xticks(x, rotation='90')
# 设置为轻型布局
plt.tight_layout()
# 显示图
plt.show()
