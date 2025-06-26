"""
循环语句for
"""
print("---str循环---")
for i in 'hello':
    print(i)
# h
# e
# l
# l
# o

print("---list循环---")
lst = [1,2,3,4]
for i in lst:
    print(i, i+10)
# 1 11
# 2 12
# 3 13
# 4 14

print("---dict循环---")
d = {'name':'laoqi', 'lang':'python', 'age':29}
for k in d:
    print(k, d[k]) # k v
# name laoqi
# lang python
# age 29

for k,v in d.items():
    print(k,v) # k v
# name laoqi
# lang python
# age 29

print("---range循环---")
for i in range(1, 5):
    print(i)
# 1
# 2
# 3
# 4

print("---将dict的k v反过来---")
d = {'name':'laoqi', 'lang':'python', 'age':29}
dt = {}
for k in d:
    dt[d[k]] = k
for i in dt:
    print(i, dt[i])
# laoqi name
# python lang
# 29 age