# -*- coding:utf-8 -*-

# 高阶函数：接受函数作为参数，或者把函数作为结果返回的函数

# 根据反向拼写给一个单词列表排序
def reverse(word):
    return word[::-1]

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits,key=reverse))

# all(iterable):如果iterable的每个元素都是真值，返回True
# any(iterable):如果iterable中有元素是真值，就返回true
