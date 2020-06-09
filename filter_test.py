#!/usr/bin/python
# -*- coding: utf-8 -*-


def is_odd(n):
    # 提取奇数
    return n % 2 ==1


# print('[1,2,3,4,5,6] 只保留奇数',list(filter(is_odd,[1,2,3,4,5,6])))

def not_empty(s):
    # 去掉首尾的空字符串
    return s and s.strip()

# print(list(filter(not_empty,['A',' ','B',None,'C',' '])))

# 求素数
"""
# 算法理解
首先，列出从2开始的所有自然数，构造一个序列：
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
不断筛下去，就可以得到所有的素数。
"""


def _odd_iter():
    # 构造从3开始的奇数序列
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    # 素数筛选函数
    return lambda x: x % n > 0


def primes():
    # 定义生成器，不断返回下一个素数
    yield 2     # 第一个素数
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)    # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)


def is_palindrome(n):
    # 回数，从左向右读和从右向左读都是一样的数
    m = int(str(n)[::-1])
    return m == n


def textis_palindrome():
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')


print('回数测试', textis_palindrome())
