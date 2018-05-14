# -*- coding:utf-8 -*-

color = ['red','green']
size = ['s','m','l']

# 列表生成式
cloths_1 = [(c,s)for c in color for s in size]
print cloths_1

'''
Python 2.x 中,在列表推导中 for 关键词之后的赋值操作可能会影响列表推导上下文中的同名变量,
但是这种情况在 Python 3 中是不会出现的。
'''

# 生成器表达式
for cloths in ((c,s) for c in color for s in size):
    print cloths

'''
用到生成器表达式之后,
内存里不会留下一个有 6 个组合的列表,因为生成器表达式会在每次 for 循环运行时才
生成一个组合。如果要计算两个各有 1000 个元素的列表的笛卡儿积,生成器表达式就可
以帮忙省掉运行 for 循环的开销,即一个含有 100 万个元素的列表。
'''