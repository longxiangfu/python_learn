"""
    功能 根据用户输入判断是人名币还是美元，然后进行汇率兑换
    作者
    版本
    时间
"""
def convert_currency(inm, vs):
    out = inm * vs
    return out

currenty_str_value = input("请输入待兑换的货币金额：")
unit = currenty_str_value[-3:]
inmoney = eval(currenty_str_value[:-3])
rmb_vs_usd = 6.77
if unit == 'CNY':
    rmb_vs_usd1 = 1 / rmb_vs_usd
elif unit == 'USD':
    rmb_vs_usd1 = rmb_vs_usd
else:
    rmb_vs_usd1 = -1

if rmb_vs_usd1 != -1:
    #函数调用
    out = convert_currency(inmoney, rmb_vs_usd1)
    print('转换后的货币金额为：', out)
else:
    print('不支持该货币')

