# -*- coding:utf-8 -*-
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

# 可以通过字段名过着位置获得信息
print tokyo.country
print tokyo[1]
print City._fields #可以通过_fields属性获得这个类的所有字段名称
data = ('Delhi NCR', 'IN', 21.935,(28.613889, 77.208889))
delhi = City._make(data) # 用 _make() 通过接受一个可迭代对象来生成这个类的一个实例,它的作用跟City(*delhi_data) 是一样的。
print delhi
print delhi._asdict() #asdict() 把具名元组以 collections.OrderedDict 的形式返回,我们可以利用它来把元组里的信息友好地呈现出来。

'''
元祖可以看成不可变的列表，除了跟增减元素相关的方法之外，元祖支持列表的其他所有方法，
还有一个例外，元组没有 __reversed__ 方法。
'''