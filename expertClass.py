#!/usr/bin/python
# -*- coding: utf-8 -*-

#   面向对象的高级编程
from types import MethodType


class Student(object):
    __slots__ = ('name', 'age', 'score', 'set_age',)
    def __init__(self,name):
        self.name = name

s = Student('Ethan')
def set_age(self, age):
    self.age = age

s.set_age = MethodType(set_age, s)  # 给实例绑定方法只对该实例有效而对其它实例无效
s.set_age(25)
# print('s.age:',s.age)
def set_score(self, score):
    self.score = score

Student.set_score = set_score   #   给类绑定方法后，所有实例均可调用
s.set_score(90)
# print('s.score:',s.score)

class Student1(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            # 类型判断
            raise ValueError('score must be an integer!')
        if value < 0 or value >100:
            # 分数值范围限制
            raise ValueError('score must between 0~100')
        self._score = value
stu1 =Student1()
stu1.set_score(96)
# print('stu1.get_score:',stu1.get_score())


class Student2(object):
    # 使用装饰器把一个方法变成属性
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            # 类型判断
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            # 分数值范围限制
            raise ValueError('score must between 0~100')
        self._score = value


stu2 = Student2()
stu2.score = 60
print('stu2.score:', stu2.score)
