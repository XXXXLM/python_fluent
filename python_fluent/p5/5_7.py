# -*- coding:utf-8 -*-

# 生成html标签
def tag(name,*content,cls=None,**attrs):
    '''
    :param name: 标签名称
    :param cls: class名称
    :param content: 标签内的内容
    :param attrs: 其他参数的名称及内容，字典形式
    :return: 生成的完整的html语句
    '''
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s" '%(attr,value)
                           for attr,value in sorted(attrs.items()))
    else:
        attr_str=''
    if content:
        return '\n'.join(' <%s%s>%s</%s> '%
                         (name,attr_str,c,name)
                         for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

if __name__ == '__main__':
    print(tag('br'))
    print(tag('p','hello'))
    print(tag('p','hello','word'))
    print(tag('p',cls='cls'))
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
                  'src': 'sunset.jpg', 'cls': 'framed'}
    print(tag(**my_tag))

'''
如果写成 def tag(name,cls=None,*content,**attrs):
不会飘红，但是执行 print(tag(**my_tag))的结果是错误的。
现在的写法执行结果是正确的，但是会飘红。
定义函数时若想指定仅限关键字参数,要把它们放到前面有 * 的参数后面。
'''
