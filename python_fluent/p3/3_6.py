# -*- coding:utf-8 -*-
'''
UserDict 并不是 dict 的子类,但是 UserDict 有一个叫
作 data 的属性,是 dict 的实例,这个属性实际上是 UserDict 最终存储数据的地方。
'''
import collections

class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, value):
        '''
        把所有的键都转成字符串
        '''
        self.data[str(key)] = value
