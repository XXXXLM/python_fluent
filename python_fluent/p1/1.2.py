# -*- coding:utf-8 -*-
from math import hypot

class VectorSelf:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r,%r)'%(self.x,self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def mul(self,param):
        return Vector(self.x*param, self.y*param)

    def mo(self):
        return hypot(self.x,self.y)

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        '''
        定义__repr__得到字符串形式的对象,
        如果没有实现 __repr__,当我们在控制台里打印一个向量的实例时,
        得到的字符串可能会是 <Vector object at 0x10e100070>。
        :return: 
        '''
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        '''
        abs 是一个内置函数,如果输入是整数或者浮点数,它返回的是输入值的绝对值;如果输
        入是复数(complex number),那么返回这个复数的模。为了保持一致性,我们的 API 在
        碰到 abs 函数的时候,也应该返回该向量的模
        :return: 
        '''
        return hypot(self.x, self.y)

    def __bool__(self):
        '''
        如果一个向量的模是 0,那么就返回 False,其他情况
        则返回 True。因为 __bool__ 函数的返回类型应该是布尔型,所以我们通过
        bool(abs(self)) 把模值变成了布尔值。
        :return: 
        '''
        return bool(abs(self))
        # 这是一种更高效的方法
        # return bool(self.x or self.y)

    # 使得类对象可以使用+
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # 使得类对象可以使用*
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


a = Vector(2,3)
b = Vector(3,4)
c = Vector()
d = VectorSelf(2,3)
e = VectorSelf(3,4)
f = VectorSelf(0,0)
print a+b
print d+e
print abs(b)
print e.mo()
print abs(c) #0
print bool(c) #true
print bool(f) #true
print a*2
print d.mul(2)

'''
默认情况下,我们自己定义的类的实例总被认为是真的,除非这个类对 __bool__ 或者
__len__ 函数有自己的实现。bool(x) 的背后是调用 x.__bool__() 的结果;如果不存
在 __bool__ 方法,那么 bool(x) 会尝试调用 x.__len__()。若返回 0,则 bool 会返回
False;否则返回 True。

我对这段话的理解是：默认情况下，实例化的类对象使用bool(x)的时候，返回的总是true,
但是我们现在的需求是在向量的模为0的时候，bool(x)返回false,所以定义了__bool__函数，
但是我用debug模式调试的时候，bool(c)并没有调用到上面写的__bool__,而且返回的也是true,
是我哪里写的不对吗
'''