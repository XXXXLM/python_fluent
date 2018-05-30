# -*- coding:utf-8 -*-

import os

fp = open('cafe.txt', 'w', encoding='utf_8')
print(fp)
fp.write('café')
# 如果没有关闭文件 os.stat('cafe.tat').st_size为0
fp.close()
print(os.stat('cafe.txt').st_size)
fp2 = open('cafe.txt')
print(fp2)
print(fp2.encoding)
print(fp2.read())
fp2.close()
fp3 = open('cafe.txt', 'rb')
print(fp3.read())