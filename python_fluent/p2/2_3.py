# -*- coding:utf-8 -*-
'''
元祖不单单是不可变的列表，元祖内的信息是和他们的位置有关的
'''

# 可以用*运算符把一个可迭代对象拆开作为函数的参数
print divmod(20,8)
t = (20,8)
print divmod(*t)
quotient,_ = divmod(*t)
print quotient
# 在进行拆包的时候,我们不总是对元组里所有的数据都感兴趣,_ 占位符能帮助处理这种情况

#(python3) 在平行赋值中,* (eg:*args)前缀只能用在一个变量名前面,但是这个变量可以出现在赋值表达式的任意位置

'''
接受表达式的元组可以是嵌套式的,例如 (a, b, (c, d))。只要这个接受元组的嵌套结
构符合表达式本身的嵌套结构,
'''
metro_areas = [
('Tokyo','JP',36.933,(35.689722,139.691667)),
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
