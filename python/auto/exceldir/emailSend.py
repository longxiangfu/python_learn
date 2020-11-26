"""
Excel自动处理并发送邮件
"""

import pandas as pd
import os
import yagmail


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
    # 读入总数据
    data = pd.read_excel(excel_path)

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
        # df = data[data['负责人'] == name]
        df = data.loc[data['负责人'] == name]
        file_path = os.path.join(dirname, f'{name}.xlsx')
        writer = pd.ExcelWriter(file_path)
        df.to_excel(writer, 'Sheet1')
        writer.save()
        if email:
            """
            发送邮件
            """
            send_email(name, email, file_path)
            print(f'已发送邮件给{name}')


if __name__ == '__main__':
    main()