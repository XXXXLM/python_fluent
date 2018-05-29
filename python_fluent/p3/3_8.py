# -*- coding:utf-8 -*-
from unicodedata import name

# 创建set的方法
s = {1,2,3}  # 等同于set([1,2,3])，但是这个方法更慢一些

# 集合推导
# chr() 0-255的整数做参数，返回一个对应的字符
j = {chr(i) for i in range(32,256) if 'SIGN' in name(chr(i),'')}
print(j)