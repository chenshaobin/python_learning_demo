#!/usr/bin/python
# -*- coding: utf-8 -*-

from functools import reduce
import logging
logging.basicConfig(level=logging.INFO)  # 指定记录信息的级别
import pdb
'''
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ZeroDivisionError as e:
    # 错误执行代码块,所有的错误类型都继承自BaseException
    # 捕获错误可以跨越多层调用
    print('ZeroDivisionError:', e)
except ValueError as e:
    print('ValueError:', e)
else:
    # 没有错误发生时执行
    print('no error!')
finally:
    print('finally...')
print('END')
'''


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as err:
        # 使用python内置的logging模块可以非常容易地记录错误信息.
        logging.exception(err)


# main()
# print('END')


# 要抛出错误，首先根据需要，先定义一个错误的class，选择好继承关系，然后用raise语句抛出一个错误的实例
# 如果可以的话尽量选择Python内置的错误类型,必要的时候才定义我们自己的错误类型
class FooError(ValueError):
    pass


def foo2(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

# foo2('0')

# 当前函数不知道应该怎么处理错误时，会继续往上抛错误，让顶层调用者去处理该错误
def foo3(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar2():
    try:
        foo3('a')
    except ValueError as e:
        print('ValueError!')
        raise

# bar2()

# 分析异常信息，定位出错误源头,并修复
'''
def str2num(s):
    return int(s)
    # 修复如下
    # if isinstance(s, int):
    #     return int(s)
    # else:
    #     return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def calcSum():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 = ', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

calcSum()
'''
# 使用断言assert来代替print()来辅助查看的地方

def foo4(s):
    n = int(s)
    assert n != 0, 'n is zero！'
    return 10 / n

def main2():
    foo4('0')

# main2()

# 使用logging调试代码,logging才是终极武器
'''
s = int('0')
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
'''


# 启动Python的调试器pdb进行调试
s = int('0')
n = int(s)
pdb.set_trace()  # 在可能出错的位置设置断点
print(10 / n)
