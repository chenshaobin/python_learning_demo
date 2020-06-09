#!/usr/bin/python
# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name, score, gender):
        # 属性的名称前加上两个下划线__就变成了一个私有变量
        self.__name = name
        self.__score = score
        self.__gender = gender

    def print_score(self):
        # print('%s: %s' % (self.name, self.score))
        print('%s :%s' %(self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_gender(self):
        return self.__gender

    def set_gender(self,newgender):
        if newgender == 'male' or 'female':
            self.__gender = newgender
        else:
            print('type error')

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
         if self.__score >=90:
             return 'A'
         elif self.__score>=80:
             return 'B'
         elif self.__score>=60:
             return 'C'
         else :
             return 'D'

'''

bart = Student('Bart Simpson', 59,'male')
lisa = Student('Lisa Simpson', 87,'female')
bart.print_score()
print('等级', bart.get_grade())
lisa.print_score()
print('等级', lisa.get_grade())
bart.set_score(98)
print('bart.score:',bart.get_score())
# 外部访问双下划线开头的实例变量，但是强烈不建议这么干
# print('(外部强制访问内部变量)bart._Student__name:',bart._Student__name)

if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
        
'''
# 继承和多态
class Animal(object):
    def run(self):
        print("Animal is running...")

class Dog(Animal):
    def run(self):
        print("Dog is running...")
    def eat(self):
        print('Eating meat...')

dog = Dog()
dog.run()
# 通过 isinstance(变量名，类型)判别变量类型


class StudentInfo(object):
    count = 0   # 每创建一个实例，该属性自动增加：

    def __init__(self, name):
        self.name = name
        StudentInfo.count += 1

nick = StudentInfo('nick')
bob = StudentInfo('bob')
smith = StudentInfo('smith')
robert = StudentInfo('robert')
scott = StudentInfo('scott')

print(StudentInfo.count)
