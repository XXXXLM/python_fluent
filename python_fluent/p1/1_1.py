# -*- coding:utf-8 -*-

import collections
from random import choice

# namedtuple用于创建只有少数属性但是没有方法的类
Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
# 因为定义了__len__方法，所以这里才可以调用len()
print len(deck)
# 因为__getitem__把[]操作交给了self._cards，所以类对象支持切片操作
print deck[0]
print deck[:2]

suit_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value*len(suit_values) + suit_values[card.suit]

for card in sorted(deck,key=spades_high):
    print card

'''
因为实现了__getitem__函数，所以deck变成了一个可迭代的对象
sorted(iterable[, cmp[, key[, reverse]]]) 
cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
'''