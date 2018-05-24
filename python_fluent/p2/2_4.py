# -*- coding:utf-8 -*-

'''
为什么切片和区间会忽略最后一个元素
1.当只有最后一个位置信息时,我们也可以快速看出切片和区间里有几个元
素:range(3) 和 my_list[:3] 都返回 3 个元素。
2.当起止位置信息都可见时,我们可以快速计算出切片和区间的长度,用后一个数减去
第一个下标(stop - start)即可。
3.这样做也让我们可以利用任意一个下标来把序列分割成不重叠的两部分,只要写成
my_list[:x] 和 my_list[x:] 就可以了
'''

# s[a:b:c] 对s在a和b之间以c为间隔取值。如果c的值为负数，以为着反向取值
# s[a:b:c] 求值时会调用s.__getitem__(slice(a,b,c))

invoice = """
0.....6................................40........52...55........
1909  Pimoroni PiBrella                    $17.50    3    $52.50
1489  6mm Tactile Switch x20                $4.95    2     $9.90
1510  Panavise Jr. - PV-201                $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240               $34.95    1    $34.95
"""
sku = slice(0,6)
des = slice(6,40)
unit_price = slice(40,52)
quantity = slice(52,55)
time = slice(55,None)
line_item = invoice.split('\n')[2:]
# print(line_item)
# for item in line_item:
#     print(item[des])

lst = list(range(10))
lst[2:5] = [1,2]
print(lst)
del lst[7:9]
print(lst)
# 等号右边的数量要和左边的长度一样
lst[2::2]=[11,22,33]
print(lst)
# 如果赋值的对象是一个切片，那么肤质语句右边必须是个可迭代对象
