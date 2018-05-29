# -*- coding:utf-8 -*-

'''
__missing__
        基类dict并没有定义这个方法，但是dict知道有这个方法的存在。如果有一个类
    继承dict，然后这个继承类提供了__missing__方法，那么在 __getitem__ 碰到找不
    到的键的时候,Python 就会自动调用它。
        __missing__ 方法只会被 __getitem__ 调用(比如在表达式 d[k] 中)。
    提供 __missing__ 方法对 get 或者 __contains__(in 运算符会用到这个方法)这
    些方法的使用没有影响。
'''
class StrKeyDict0(dict):

    def __missing__(self, key):
        '''
        如果找不到的键不是字符串，则转换成他的字符串形式再查找，
        如果是字符串则抛出KeyError.
        为什么要判断key是不是字符串：
        如果没有这个测试,只要 str(k) 返回的是一个存在的键,那么 __missing__ 方法是没
        问题的,不管是字符串键还是非字符串键,它都能正常运行。但是如果 str(k) 不是一个
        存在的键,代码就会陷入无限递归。这是因为 __missing__ 的最后一行中的
        self[str(key)] 会调用 __getitem__,而这个 str(key) 又不存在,于是
        __missing__ 又会被调用。
        '''
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]

    def get(self,key,default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        '''
        为了保持一致性,__contains__ 方法在这里也是必需的。这是因为 k in d 这个操作会
        调用它,但是我们从 dict 继承到的 __contains__ 方法不会在找不到键的时候调用
        __missing__ 方法。__contains__ 里还有个细节,就是我们这里没有用更具 Python 风
        格的方式——k in my_dict——来检查键是否存在,因为那也会导致 __contains__ 被
        递归调用。为了避免这一情况,这里采取了更显式的方法,直接在这个 self.keys() 里
        查询。
        在python3中，k in dict.keys操作是很快的，因为dict.keys()的返回值是一个“视图”，
        python2中，dict.keys()返回的是一个列表
        '''
        return key in self.keys() or str(key) in self.keys()

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[4])
# print(d[1])
print(d.get('2'))
print(d.get(4))
print(d.get(1))
print(2 in d)
print(1 in d)