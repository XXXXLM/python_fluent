# -*- coding:utf-8 -*-

cafe = bytes('cafe', encoding='utf-8')
print(cafe)
print(cafe[0])
print(cafe[:1])
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])

# cafe[0]获得的是一个整数，而cafe[:1]返回的是一个长度为1的bytes对象，这种情况
# 只对str这个序列成立