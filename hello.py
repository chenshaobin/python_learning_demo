# -*- coding: utf-8 -*-
import math
from functools import reduce

"""
names = ['Michael', 'Bob', 'Ethan']
for name in names:
    print(name)

"""
"""
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
"""
"""
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n-2
print(sum)
"""
"""
d = {'Michael': 95, 'Bob': 75, 'Ethan': 95, 'test': (1, [2, 3])}
print('d',d)
print(d['test'])
print('Thmoas' in d)

"""
"""
s = set([1, 2, 3])
print(s)
"""

"""
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-100))


def nop():
    # 做占位符
    pass
"""

"""
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


a, b = move(100, 100, 60, math.pi / 6)
print(a, b)
r = move(100, 100, 60, math.pi / 6)
print('r=', r)
"""

"""
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print('5*5=', power(5, 2))
"""


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


"""
nums = [1, 2, 3]
print(calc(*nums))
"""

"""
def product(x, *y):
    # 计算多个数的乘积
    s = 1
    if not y:
        s = s * x
    else:
        s = s * x
        for k in y:
            s = s * k
    return s
"""

"""
print('product(2,5,6)', product(2, 5, 6))
print('product(1,5) =', product(1, 5))
"""


"""
def fact(n):
   return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact(4))
"""


"""
def move(n, a, b, c):
    # 汉诺塔问题
    if n == 1:
        print(a, '--->', c)
    else:
        move(n-1, a, c, b)
        print(a, '--->', c)
        move(n-1, b, a, c)


move(3, 'A', 'B', 'C')
"""


"""
# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other', kw)


extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Ethan', 20, city=extra['city'])
person('Ethan', 20, **extra)
"""

"""
# 命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')
"""

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[-2:-1])
# L2 = list(range(100))
# print(L2[:10:2])


def trim(s):
    # 去除字符串首尾空格，递归函数
    if len(s) > 0:
        if s[0] == '':
            return trim(s[1:])
        elif s[-1] == '':
            return trim(s[:-1])
    return s


# print('   123abc    去除首尾空格', trim("   123abc    "))
"""
d = {'a': 1, 'b': 2, 'c': 3}
print('d.items():', d.items())
for key, v in d.items():
    print(key + ':' + str(v))
"""


def findMinAndMax(l):
    if len(l) == 0:
        return (None, None)
    max = min = l[0]
    for i in L:
        if isinstance(i, int or float):
            if i > max:
                max = i
            elif i < min:
                min = i
        else:
            raise TypeError
    return min, max

# 使用列表生成式
# print('[1,45,59,0,89,48151]',findMinAndMax([1,45,59,0,89,48151]))
# print('生成x*x的列表', [x * x for x in range(1,11) if x % 2 == 0] )
# print('两层循环生成全排列',[m + n for m in 'ABC' for n in 'XYZ'])
import os
# print('列出当前目录下的所有文件和目录名',[d for d in os.listdir('.')])
d = {'a': '1', 'b': '2', 'c': '3'}
# print('使用两个变量生成字符串列表',[k +'='+ v for k, v in d.items()])
Lstring = ['Hello', 'World', 'IBM', 'Apple']
# print('将list中的所有字符串变成小写',[s.lower() for s in Lstring])
Llist = ['Hello', 'World', 18, 'Apple', None]
# print('将list中的字符串小写输出，其它类型数据去除',[l.lower() for l in Llist if isinstance(l, str)])
g = (x * x for x in range(10))
# print((x * x for x in g))
# print(next(g))


def printgenerator():
    g = (x * x for x in range(10))
    for n in g:
        print('值', n)

# print(printgenerator())

def fib(max):
    # max为数值个数
    # 斐波拉契数列
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'

# print('fib(6)',fib(6))
def printfFib():
    for n in fib(6):
        print(n)

# print('fib(6)打印值',printfFib())

def f(x):
    return x * x

r = map(f, [1,2,3,4,5,6])
# print(r)
# print(list(r))



def add(x, y):
    return x +y

a = reduce(add, [1, 3, 5, 7, 9])
# print(a)

def count():
    fs=[]
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

# f1,f2,f3,= count()
# print(f1())
# print(f3())

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs =[]
    for i in range(1, 4):
        fs.append(f(i))
    return fs

# f1,f2,f3,= count()
# print(f1())
# print(f2())
# print(f3())


def createCounter():
    i = [0]

    def counter():
        i[0]+=1
        return i[0]
    return counter


def test_createCounter():
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')

# print(test_createCounter())


class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
