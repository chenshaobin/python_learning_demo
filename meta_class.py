#!/usr/bin/python
# -*- coding: utf-8 -*-

from hello import Hello
# h = Hello()
# h.hello()
# # type 函数可以查看一个类型或变量的类型
# print('type of Hello', type(Hello))  # Hello 是一个class，它的类型就是type
# print('type of h', type(h))     # h是一个实例，它的类型就是Class Hello

# 使用type动态创建class
'''
    要创建一个class对象，type()函数依次传入3个参数：
    (1)class的名称；
    (2)继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    (3)class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello

'''
def fn(self, name='world'):
    # class中将会使用的函数
    print('Hello, %s.' % name)

Hello_type = type('Hello_type', (object,), dict(hello=fn))
h_type = Hello_type()
h_type.hello()
