# -*- coding:utf-8 -*-

# unicode encode error的处理方式
city = 'São Paulo'
# ignore跳过无法编码的字符
print(city.encode('cp437', errors='ignore'))
# replace用?代替无法编码的字符
print(city.encode('cp437', errors='replace'))
# xmlcharrefreplace 把无法编码的字符替换成XML实体
print(city.encode('cp437', errors='xmlcharrefreplace'))

# unicode decode error的处理方式
octets = b'Montr\xe9al'
# 使用 replace 无法解码的替换成�，这是官方指定的
print(octets.decode('utf-8',errors='replace'))