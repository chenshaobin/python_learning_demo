#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
# json表现出来就是一个字符串
"""
    # dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object
"""
# Python对象到JSON格式的转换
"""
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))
"""

"""
    # 把JSON反序列化为Python对象
    # 用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
"""

"""
json_str = '{"name": "Bob", "age": 20, "score": 88}'
print(json.loads(json_str))  # {'name': 'Bob', 'age': 20, 'score': 88}
"""

"""
# 将class实例对象转化为可序列化json的对象
# json.dumps()函数的可选参数default就是把任意一个对象变成一个可序列为JSON的对象
"""
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Ethan', 20, 88)
# print('class to JSON对象：',json.dumps(s, default=student2dict))

# 另外，可以把任意class的实例变为dict
# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
# 也有少数例外，比如定义了__slots__的class
print('class to JSON对象,使用_dict__属性：', json.dumps(s, default=lambda obj: obj.__dict__))

# 将一个JSON反序列化为一个对象实例,loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例
def dict2Student(d):
    return Student(d['name'], d['age'], d['score'])

json_class_str = '{"name": "Ethan", "age": 20, "score": 88}'
print(json.loads(json_class_str, object_hook=dict2Student))
