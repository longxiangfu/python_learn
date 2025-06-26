"""
str
"""
print("---dir 查看方法---")
s = "python lesson"
print(dir(s))

print("---index 某str的索引---")
print(s.index("n")) # 5
print(s.index("n", 6)) # 12  第二个参数是开始索引

print("---split 分割成列表---")
a = "I Love Python"
print(a.split(" ")) # ['I', 'Love', 'Python']
print(type(a.split(" "))) # <class 'list'> 列表

print("---join 列表连接成字符串---")
lst = a.split(" ")
print("-".join(lst)) # I-Love-Python

"""
格式化，冒号左面数字表示第几个参数，冒号右边数字表示位数，>表示右对齐，
^表示居中对齐，d表示数字，f表示浮点数，.1f表述浮点数保留1位
*args: 任意数量的位置参数
*kwargs: 任意数量的关键字参数
"""
print("---format 格式化字符串---")
print("I like {0} and {1}".format("python", "java")) # I like python and java
print("I like {0:10} and {1:>15}".format("python", "java")) # I like python     and            java
print("I like {0:^10} and {1:>15}".format("python", "java")) # I like   python   and            java
print("She is {0:10d} years old and {1:.1f}m in height".format(28, 1.68)) # She is         28 years old and 1.7m in height
print("I like eat {fruit} and {shucai}".format(fruit="apple", shucai="tomato")) # I like eat apple and tomato

