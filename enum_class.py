#!/usr/bin/python
# -*- coding: utf-8 -*-

# 使用枚举类
from enum import Enum,unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):
    # 使用装饰器@unique可以帮助我们检查保证没有重复值
    # Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
# print(day1)
# print(Weekday(1))
# for name, member in Weekday.__members__.items():
#     print(name, '=>', member)

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if isinstance(gender, Gender):
            self._gender = gender
        if isinstance(gender, int):
            if gender == 0:
                self._gender = Gender.Male
            elif gender == 1:
                self._gender = Gender.Female
            else:
                raise ValueError("The value of gender can only be '0' or '1’'!'")

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
