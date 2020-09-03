"""
对用户输入进行大小写转换
"""

word = input("请输入字符串:")
lst = []
for i in word:
    if i.islower():
        lst.append(i.upper())
    else:
        lst.append(i.lower())
new_word = "".join(lst)
print(word, "==>", new_word)
