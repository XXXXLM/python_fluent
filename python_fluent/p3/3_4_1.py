# -*- coding: utf-8 -*-

'''
在实例化一个defaultdict的时候，需要给构造方法提空一个可调用对象，这个可调用对象
会在__getitem__碰到找不到的键的时候被调用，让__getitem__返回这个默认值。
defaultdict 里的 default_factory 只会在 __getitem__ 里被调用,在其他的方法里完全
不会发挥作用。比如,dd 是个 defaultdict,k 是个找不到的键, dd[k] 这个表达式会调用
default_factory 创造某个默认值,而 dd.get(k)则会返回 None。
'''

import sys
import re
import collections

WORD_RE = re.compile(r'\w+')
# 把list构造方法作为default_factory创建defaultdict
index = collections.defaultdict(list)

with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])