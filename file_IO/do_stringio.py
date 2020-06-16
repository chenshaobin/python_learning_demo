#!/usr/bin/python
# -*- coding: utf-8 -*-

from io import StringIO
# 从内存中读写str数据
"""
f = StringIO()
f.write('hello')
print(f.getvalue())

"""

# 读取StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
