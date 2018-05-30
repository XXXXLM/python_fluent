# -*- coding:utf-8 -*-
from unicodedata import normalize, name

s1 = 'café'
s2 = 'cafe\u0301'
print(s1, s2)
print(s1 == s2)
# NFC 使用最少的码位构成等价的字符串
print(len(normalize('NFC',s1)), len(normalize('NFC',s1)))
# NFD 把组合字符分解成基字符和单独的组合字符
print(len(normalize('NFD',s1)), len(normalize('NFD',s1)))
print(normalize('NFC',s1) == normalize('NFC',s2))
print(normalize('NFD',s1) == normalize('NFD',s2))
o = '\u2126'
print(o)
print(name(o))
o_c = normalize('NFC', o)
print(o_c)
print(name(o_c))
print(normalize('NFC', o) == normalize('NFC', o_c))
'''
在 NFKC 和 NFKD 形式中,各个兼容字符会被替换成一个或多个“兼容分解”字符,即便
这样有些格式损失,但仍是“首选”表述——理想情况下,格式化是外部标记的职责,不应
该由 Unicode 处理。
'''
