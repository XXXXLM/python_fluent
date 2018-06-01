# -*- coding:utf-8
import random

class BingoCage:

    def __init__(self,items):
        self._item = list(items)
        random.shuffle(self._item)

    def pick(self):
        try:
            return self._item.pop()
        except IndexError:
            raise LookupError('empty BingoCage')

    def __call__(self):
        '''实现 __call__ 方法的类是创建函数类对象的简便方式'''
        return self.pick()

bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())
print(callable(bingo)) #因为实现了__call__方法，使得类对象变成可调用的