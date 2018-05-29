# -*- coding:utf-8 -*-

s = 'hello'
print(len(s))
print(type(s))
b = s.encode('utf8')
print(b)
print(type(b))
a = b.decode('utf8')
print(b)
print(a)
print(type(a))


# decode 返回的是一个新的对象吗？？？