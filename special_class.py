#!/usr/bin/python
# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        # 打印实例
        return 'Student object (name:%s)' % self.name

    __repr__ = __str__  # __repr__是为调试服务的

    def __getattr__(self, attr):
        # 当调用不存在的属性时，就会试图调用该函数获取属性
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25  # 返回函数
        raise AttributeError('\'Student\' object has no attribute \'%s\' ' % attr)


# print(Student('Ethan'))
# s = Student('Ethan')
# print(s.className) # 调用不存在的属性
# print('在实例本身上调用实例方法:', s())


class Chain(object):
    # 动态链式调用
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, path):
        # 在实例本身上调用实例方法，可传入参数
        # print('My name is %s.' % self.name)
        return Chain('%s/%s' % (self._path, path))

    __repr__ = __str__


# print('动态链式调用：', Chain().status.user.timeline.list)
print(Chain().users('Ethan').repos)


class Fib(object):
    # 斐波那契数列
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        #   可通过索引获取某一项,传入参数可以是一个int类型，也可以是一个切片对象slice
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


# f = Fib()
# print(f[:10])
