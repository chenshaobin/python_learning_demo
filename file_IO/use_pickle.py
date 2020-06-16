#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle

# d = dict(name='Bob', age=20, score=88)
"""
    # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
    # 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
"""

# print(pickle.dumps(d))
"""
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
"""

"""
    # 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
    # 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
"""

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

