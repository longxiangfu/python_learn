"""
python导入
"""
from foundation2.twoDir.classTest8 import Foo
from foundation2.twoDir.classTest8 import f
from foundation2.twoDir.classTest8 import xx
from foundation2.twoDir.classTest8 import myMethod

print("---自定义的引入---")
print(Foo.name)
print(f.name)
print('xx=' + str(xx))
myMethod()


print("---标准库引入---")
import math
from math import pow
import math as shuxue

math.pow(2, 3)
pow(2, 3)
shuxue.pow(2, 3)


print("---查看python的系统路径---")
import sys
print(sys.path)
