"""
    功能
    作者
    版本
    时间
"""
#人民币和美元汇率兑换
rmb_str_value = input("请输入人民币金额: ")
rmb_value = eval(rmb_str_value)
usd_vs_rmb = 6.77
usd_value = rmb_value / usd_vs_rmb
print("美元金额为：", usd_value)