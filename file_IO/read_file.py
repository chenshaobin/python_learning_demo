#!/usr/bin/python
# -*- coding: utf-8 -*-

# f = open('test.txt', 'r')
# print(f.read())
# f.close() # 文件使用完毕之后必须关闭

# 使用 with语句来自动帮我们调用close()方法

with open('test.txt', 'r') as f:
    print(f.read())

# read(size)方法:每次最多读取size个字节的内容。
# readline()：可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list

# 打开二进制文件
# f = open('test.JPG', 'rb')
# print(f.read())
# f.close()

# 读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
