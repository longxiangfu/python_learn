"""
    功能 根据用户输入判断是人名币还是美元，然后进行汇率兑换
    作者
    版本
    时间
"""
currenty_str_value = input("请输入待兑换的货币金额: ")
unit = currenty_str_value[-3:]
if unit == 'CNY':
    rmb_str_value = currenty_str_value[:-3]
    rmb_value = eval(rmb_str_value)
    usd_vs_rmb = 6.77
    usd_value = rmb_value / usd_vs_rmb
    print('兑换后的美元为：', usd_value)
elif unit == 'USD':
    usd_str_value = currenty_str_value[:-3]
    usd_value = eval(usd_str_value)
    usd_vs_rmb = 6.77
    rmb_value = usd_value / usd_vs_rmb
    print('兑换后的人民币为：', rmb_value)
else:
    print("该程序目前版本尚不支持该货币")