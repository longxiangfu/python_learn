"""
Pandans读写excel
"""

import pandas as pd


def writeExcel():
    # DataFrame 数据帧 相当于工作蒲中的一个工作表
    df = pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['zhangsan', 'lisi', 'wangwu'],
        'age': [26, 38, 24],
        'score': [89, 90, 85]
    })
    print(df)


    # 自定义索引，不然pandas会使用默认的索引，这会导致生成的工作表也会存在这些索引
    df = df.set_index('id') # 设置id列为索引列
    print(df)

    # 将数据写入到excel
    df.to_excel('people.xlsx')
    print('Done!')


def readExcel():
    path = "people.xlsx"
    # header=2 表示从第三行开始，跳过了前两行，sheetname指定读取的工作表
    # people = pd.read_excel(path, header=2, sheet_name='Sheet1')
    people = pd.read_excel(path, header=0, sheet_name='Sheet1')
    print(people)
    print(type(people)) # <class 'pandas.core.frame.DataFrame'>
    # # 列出列名
    print(people.columns) # Index(['id', 'name', 'age'], dtype='object')
    print(dir(people))
    print("--------")

    # 如果读入的excel中没有开头标题，则可以将header=None,人为地进行设置
    people1 = pd.read_excel(path, header=None)
    people1.columns = ['id', 'name', 'age']
    print(people1.columns) # Index(['id', 'name', 'age'], dtype='object')
    print("--------")

    # 指定id列为索引
    people2 = pd.read_excel(path, index_col='id')
    # 此时就不会产生默认索引了
    print(people2)
    # 输出前5行
    print(people2.head())
    print("--------")

    # skiprows 跳过头几行  dtype 设置某一列的类型
    people4 = pd.read_excel(path, skiprows=2, dtype={'id': str, 'age': int, 'name': str})
    print(people4)

    result = people2
    return result


if __name__ == '__main__':
    writeExcel()
    # people = readExcel()
    # 排序 by针对某一行排序  ascending为False表示从大到小  inplace为True表示排序后的结果又赋值给了原变量
    # people.sort_values(by='age', ascending=False, inplace=True)
    # print(people)
