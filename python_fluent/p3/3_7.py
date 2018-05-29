# -*- coding:utf-8 -*-

'''
从 Python 3.3 开始,types 模块中引入了一个封装类名叫 MappingProxyType。如果给这
个类一个映射,它会返回一个只读的映射视图。虽然是个只读视图,但是它是动态的。这
意味着如果对原映射做出了改动,我们通过这个视图可以观察到,但是无法通过这个视图
对原映射做出修改。
'''

import types

d = {1: 'A'}
d_proxy = types.MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
d[2] = 'x' # 可以通过修改原映射可以动态的反映到d_proxy上
# d_proxy[3] = 'y' 会报错，d_proxy不能直接修改
print(d_proxy)