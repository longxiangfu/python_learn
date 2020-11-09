"""
利用pandas python-docx操作excel和word，并生成工作周报
"""

import pandas as pd
import matplotlib.pyplot as plt
from docx import Document
from docx.shared import Inches

"""1.操作excel,将数据报表保存为图片"""
students = pd.read_excel("E:\\pycharmWork\\python\\auto\\people.xlsx")
students.sort_values(by='Score', inplace=True, ascending=False)
print(students)

x = range(len(students.Name))
plt.xticks(x, students.Name)
plt.bar(x, students.Score, color='orange')

plt.title('Students', fontsize=16)
plt.xlabel('name')
plt.ylabel('score')

plt.xticks(x, rotation='90')
plt.tight_layout()
image_name = 'data.jpg'
plt.savefig(image_name)

"""2.操作word"""
document = Document()
document.add_heading('数据分析报告', level=0)

first_student_name = students.iloc[0, :]['Name']
first_student_score = students.iloc[0, :]['Score']

p = document.add_paragraph('分数排在第一个的学生是')
p.add_run(str(first_student_name)).bold = True
p.add_run(',分数为')
p.add_run(str(first_student_score)).bold = True

document.add_paragraph(f'总共有{len(students.Name)}名学生参加了考试，学生考试的总体情况：')

table = document.add_table(rows=len(students.Name) + 1, cols=2)
table.style = 'LightShading-Accent1'

table.cell(0, 0).text = '学生姓名'
table.cell(0, 1).text = '学生分数'

for i, (index, row) in enumerate(students.iterrows()):
    table.cell(i+1, 0).text = str(row['Name'])
    table.cell(i+1, 1).text = str(row['Score'])

document.add_paragraph('')
document.add_picture(image_name, width=Inches(5))
document.save('Students.docx')
print('Done!!!')
