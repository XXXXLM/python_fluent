# -*- coding:utf-8 -*-

'''
collections.OrderedDict
    这个类型在添加键的时候会保持顺序,因此键的迭代次序总是一致
的。OrderedDict 的 popitem 方法默认删除并返回的是字典里的最后一个元素,但是如
果像 my_odict.popitem(last=False) 这样调用它,那么它删除并返回第一个被添加进
去的元素.
    字典是无序的，但是OrderedDict类是有序的，在添加键的时候会保持顺序。
但是初始化的时候传入多个参数，他们的顺序是随机的。
    常规dict在检查相等性时会查看其内容，OrderDict还会考虑元素添加的顺序
collections.ChainMap
    该类型可以容纳数个不同的映射对象,然后在进行键查找操作的时候,这些对象会被
当作一个整体被逐个查找,直到键被找到为止。这个功能在给有嵌套作用域的语言做解释
器的时候很有用,可以用一个映射对象来代表一个作用域的上下文。
collections.Counter
    这个映射类型会给键准备一个整数计数器。每次更新一个键的时候都会增加这个计数
器。所以这个类型可以用来给可散列表对象计数,或者是当成多重集来用——多重集合就
是集合里的元素可以出现不止一次。Counter 实现了 + 和 - 运算符用来合并记录,还有
像 most_common([n]) 这类很有用的方法。
'''

import collections

x = {'a': 1, 'b': 2}
y = {'b': 10, 'c': 11}
z = collections.ChainMap(y,x)
print(z)
# maps 返回用户可更新的映射对象列表,可更新任何一个列表里显示的映射对象
print(z.maps)
z.maps[0]['c'] = 20
print(z.maps)
# new_child(m) 创建一个新的ChainMap对象，在列表第一个元素插入映射对象m
xx = {'d': 33, 'e': 55}
z = z.new_child(xx)
print(z.maps)
# parents 返回除第一个映射对象之外的所有映射对象的ChainMap对象
z = z.parents
print(z.maps)

# Counter类的创建 可以是字符串，可迭代对象或者键值对
a = collections.Counter()
b = collections.Counter('hello')
c = collections.Counter({'a': 4, 'b': 5})
d = collections.Counter(a=4, b=3)
# 当所访问的键不存在的时候 返回0
print(b['l'])
print(b['a'])
# 使用update()增加
b.update('hi')
print(b['h'])
# 使用subtract()减少
b.subtract('hi')
print(b['h'])
# 使用del删除键，计数为0时不意味着元素被删除
del b['o']
print(b)
# elements() 返回一个迭代器，元素重复多少次，迭代器中就包含多少该元素。个数小于1的不被包含
print(list(b.elements()))
# most_common 返回一个topN列表,没有指定时，返回所有元素，元素计数相同是，排列无序
print(b.most_common(1))
# + - | & 操作也可以用于Counter &交集，返回各元素的最小值
#  | 并集 返回各元素的最大值 得到的Counter对象将会删除小于1的元素