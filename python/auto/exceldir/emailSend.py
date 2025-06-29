"""
Excel自动处理并发送邮件
# 1
>>> df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
...                   index=['cobra', 'viper', 'sidewinder'],
...                   columns=['max_speed', 'shield'])
>>> df
            max_speed  shield
cobra               1       2
viper               4       5
sidewinder          7       8

>>> df.loc[df['shield'] > 6]
            max_speed  shield
sidewinder          7       8

"""

import pandas as pd
import os
import yagmail
from pandas.core.interchange.dataframe_protocol import DataFrame


def send_email(name, to, file_path):
    """
    发送邮件
    :param name:
    :param to:
    :param file_path:
    :return:
    """
    contents = [
        f'{name},你好，您的汇报数据已整理发送到邮箱附件中',
        file_path
    ]
    yag = yagmail.SMTP(
        user='longxiangfuct@sina.com',
        password='b2f6b9beca93e3b8',
        host='smtp.sina.com'
    )
    yag.send(to=to, subject='汇报数据', contents=contents)


def main():
    """
    读入excel数据
    """
    excel_path = '渠道数据分析总表.xlsx'
    # 读入数据,返回DataFrame对象
    data_frame = pd.read_excel(excel_path)

    """
    按负责人名称拆分excel
    """
    names = {
        '翟丹': '15201220208@sina.cn',
        '陈文': '15201220208@sina.cn'
    }
    dirname = 'exceldir'
    if not os.path.exists(dirname):
        # 创建文件夹路径
        os.makedirs(dirname)
    for name, email in names.items():
        # 筛选数据。将列“负责人”=当前的name的数据筛选出来，返回DataFrame对象
        sub_data_frame = data_frame.loc[data_frame['负责人'] == name]
        # 构建文件路径
        file_path = os.path.join(dirname, f'{name}.xlsx')
        # 获取excel写入对象
        writer = pd.ExcelWriter(file_path)
        # 通过写入对象，将数据写入sheet中
        sub_data_frame.to_excel(writer, sheet_name='Sheet1')
        # 保存文件
        writer._save()
        if email:
            """
            发送邮件
            """
            # send_email(name, email, file_path)
            print(f'已发送邮件给{name}')


if __name__ == '__main__':
    main()