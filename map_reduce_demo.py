#!/usr/bin/python
# -*- coding: utf-8 -*-
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num2(s):
        return DIGITS[s]

    return reduce(fn, map(char2num2, s))

# print('将字符串123456转整数',str2int('123456'))


def char2num(s):
    return DIGITS[s]

def str2intdemo2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# print('将字符串123456转整数',str2intdemo2('123456'))


def normlize(name):
    # 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
    if not isinstance(name, str):
        raise TypeError("please enter a String")
    return name[0].upper() + name[1:].lower()

def normlizeNameList(list):
    return map(normlize,list)

print(list(normlizeNameList(['ethan','ETHAN','eThan'])))


def prod(list):
    # 接受一个list并利用reduce()求积
    return reduce(lambda x, y :x * y,list)

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def str2float(s):
    # 利用map和reduce编写一个把字符串'123.456'转换成浮点数123.456的函数
    def char2num(s):
        return DIGITS[s]
    i = s.find('.')
    L1 = reduce(lambda x, y:x* 10 + y,map(char2num,s[:i])) # 取'.'之前的数计算
    L2 = reduce(lambda x ,y :x/10 + y,map(char2num,s[:i:-1]))/10  #倒数取数
    return L1 + L2

print('str2float(\'123.456\')= ',str2float('123.456'))