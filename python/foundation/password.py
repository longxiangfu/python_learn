"""
利用凯撒密码方案将用户输入进加密
"""

letter = input("请输入：")
'编码'
pwd = ord(letter) + 3
'解码'
pwd_letter = chr(pwd)
print(letter, "==>", pwd_letter)
