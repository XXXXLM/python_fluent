# -*- coding:utf-8 -*-

#  +和*操作都不会改变原来的列表，而是会生成一个新的序列

'''
如果序列里面是元素是对其他可变对象的引用的话，使用*的时候就需要注意，
比如[[]]*3，得到的列表里面包含的三个元素其实是三个引用，而且这三个引用只想
的是同一个列表。
'''

def correct():
    borad = [['_'] * 3 for i in range(3)]
    print(borad)
    borad[1][1] = 'x'
    print(borad)
    '''
    相当于：
    board = []
    for i in range(3):
        row = ['_'] * 3
        board.append(row)
    每次迭代时都会创建一个新的列表，每次追加的都是不同的对象
    '''

def error():
    weird_board = [['_'] * 3] * 3
    print(weird_board)
    weird_board[1][1] = 'e'
    print(weird_board)
    '''
    weird_board其实包含了3个指向同一个列表的引用，当我们尝试去修改
    一个值的时候就能发现三个引用指向同一个对象，相当于
    row = ['_'] * 3
    board = []
    for i in range(3):
        board.append(row)
    每次追加的都是同一个对象
    '''

correct()
error()