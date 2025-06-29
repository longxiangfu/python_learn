import pandas as pd
import matplotlib.pyplot as plt


def draw_bar(file_path: str, title: str, x_label: str, y_label: str, bar_color: str = 'orange'):
    """
    绘制柱状图

    参数:
        file_path (str): Excel文件路径，包含要绘制的数据
        title (str): 图表标题
        x_label (str): x轴标签
        y_label (str): y轴标签
        bar_color (str, 默认值='orange'): 柱子的颜色

    返回值:
         tuple[pyplot.py, DataFrame]
    """

    df = pd.read_excel(file_path)
    df.sort_values(by='score', inplace=True, ascending=False)

    x = range(len(df.name))
    print("x:", x)  # x: range(0, 3)
    # 设置x轴的标记位，以及标记位的标签
    plt.xticks(x, df.name)

    # 将x轴标签旋转90度，便于显示长的标签
    plt.xticks(x, rotation=90)

    # 定义条形图
    plt.bar(x, df.score, color=bar_color)

    # 定义标题、x轴标签和y轴标签
    plt.title(title, fontsize=16)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # 设置为轻型布局
    plt.tight_layout()

    return plt,df



if __name__ == '__main__':
    file_path = 'people.xlsx'
    title = 'Students'
    x_label = 'name'
    y_label = 'score'
    result_tuple = draw_bar(file_path, title, x_label, y_label)
    result_tuple[0].show()