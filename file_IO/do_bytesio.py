#!/usr/bin/python
# -*- coding: utf-8 -*-

# 内存中操作二进制数据
from io import BytesIO
# 写入字节数据
f = BytesIO()
f.write('中文'.encode('utf-8'))  # 写入的数据为经过UTF-8编码的bytes
print(f.getvalue())

# 读取数据
f1 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f1.read())
