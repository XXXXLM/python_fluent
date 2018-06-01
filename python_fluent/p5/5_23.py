# -*- coding:utf-8 -*-

# 高阶函数：接受函数作为参数，或者把函数作为结果返回的函数

# 根据反向拼写给一个单词列表排序
def reverse(word):
    return word[::-1]

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits,key=reverse))

# all(iterable):如果iterable的每个元素都是真值，返回True
# any(iterable):如果iterable中有元素是真值，就返回true
fruits.append('0')
print(fruits)
print(all(fruits))
print(any(fruits))

'''
Python 简单的句法限制了 lambda 函数的定义体只能使用纯表达式。换句话
说,lambda 函数的定义体中不能赋值,也不能使用 while 和 try 等 Python 语句
'''
print(sorted(fruits,key=lambda word:word[::-1]))
