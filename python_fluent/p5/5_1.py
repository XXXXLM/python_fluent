# -*- coding:utf-8 -*-

'''
一等对象：
    在运行时创建
    能赋值给变量或数据结构中的元素
    能作为参数传给函数
    能作为函数的返回结果
'''

def factorial(n):
    ''' return n! '''
    return 1 if n < 2 else n * factorial(n-1)

if __name__ == '__main__':
    # 把factorial赋值给变量fact
    fact = factorial
    print(fact)
    print(fact(5))
    lst1 = list(map(fact,range(10)))
    lst2 = [fact(n) for n in range(10)]
    print(lst1 == lst2)
    lst3 = list(map(fact,filter(lambda n : n%2, range(10))))
    lst4 = [fact(n) for n in range(10) if n%2]
    print(lst3 == lst4)

    # map和filter返回生成器，所以他们的直接替代品就是生成器表达式
