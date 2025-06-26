"""
str
"""
print("---len---")
a = "hello world"
print(len(a)) # 11

print("---index---")
print(a[0]) # h
print(a[-1]) # d
print(a[7]) # o

print("---截取子串---")
print(a[1:7]) # ello w
print(a[1:7:2]) #el   最后的2表示步长