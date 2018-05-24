# -*- coding:utf-8 -*-

'''
    list.sort 就地排序，不会生成新的列表，返回值是none,
    sorted 新建一个列表作为返回值，可以接受任何形式的可迭代对象
作为参数，包括不可变序列和生成器。不管参数是什么形式，返回的都是列表。
    但是这两个都有两个可选的关键字参数
    reverse:默认为False升序
    key:一个只有一个参数的函数，这个函数会被用到序列的每一个元素上，
所产生的结果将是排序算法依赖的对比关键字。这个参数的默认值是恒等函数，
也就是默认用元素自己的值来排序。
'''

letter = ['a','cd','bcd','defg']
# 按照字母顺序排列
print(sorted(letter))
# 按照字母降序排列
print(sorted(letter,reverse=True))
# 按照字母长度排序
print(sorted(letter,key=len))
# 打印列表，发现列表没有发生变化
print(letter)
letter.sort()
# 列表变化
print(letter)