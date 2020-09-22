'''
'Python' --> 'pYTHON'
演示函数定义
'''

def convert(s='python'):
    lst = [i.upper() if i == i.lower() else i.lower() for i in s]
    return "".join(lst)

s = 'Hello'
c = convert(s)
print(c)
d = convert()
print(d)