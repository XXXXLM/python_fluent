# -*- coding: utf-8 -*-

import sys
import re
WORD_RE = re.compile(r'\w+')
index = {}

with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            '''
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences
            '''
            # 获取单词的出现情况列表,如果单词不存在,把单词和一个空列表放进映射,
            # 然后返回这个空列表,这样就能在不进行第二次查找的情况下更新列表了。
            index.setdefault(word, []).append(location)


for word in sorted(index, key=str.upper):
    print(word, index[word])

'''
1. enumerate
    enumerate(seq,[start=0])
    seq :一个可迭代对象
    start :下标开始的位置
    lst = [6,7,8]
    for item in enumerate(lst):
        print(item)
    输出结果：
        (0, 6)
        (1, 7)
        (2, 8)
2. finditer
    finditer和findall很相似，但是又有很大的区别
    两者都可以获取所有的匹配结果，但是findall返回的列表，
    finditer返回的是MatchObject类型的iterator。
'''