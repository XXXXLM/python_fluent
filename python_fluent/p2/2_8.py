# -*- coding:utf-8 -*-

import bisect
import sys

haystack = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
needles = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(needles):
        position = bisect_fn(haystack,needle)
        off_set = position * ' |'
        print(ROW_FMT.format(needle,position,off_set))

def grade(score,breakpoints=[60,70,80,90],grades='FDCBA'):
    i = bisect.bisect(breakpoints,score)
    return grades[i]

if __name__ == '__main__':
    print(sys.argv[-1])
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO',bisect_fn.__name__)
    print('haystack ->',''.join('%2d' % n for n in haystack))
    demo(bisect_fn)
    print('-------------------------------')
    print([grade(score) for score in [33,55,66,88,99]])

'''
bisect模块的函数有：bisect bisect_left bisect_right insort insort_left insort_right
首先要确保操作的列表是已排序的
bisect.bisect(data,needle) 同bisect_right 返回needle在data中的位置，但是不会插入
bisect.bisect_left(data,needle) 用于有重复数值的情况，返回跟他相同的元素后面一个的位置
insort(data,needle) 同insort_right 将needle插入data中，并能保持data的升序，返回的修改后的列表
insort_left,对于有重复的数值的情况下，插入相同元素的左面
'''