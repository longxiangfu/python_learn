'''
字符串s = 'Life is short You need python',统计每个字母出现的次数
演练for
'''

s = 'Life is short You need python'
d = {}
for letter in s:
    if letter.isalpha():
        if letter in d:
            d[letter] +=1
        else:
            d[letter] =1

print(d)
