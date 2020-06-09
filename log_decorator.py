import functools

def log(func):
    # 打印日志
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' %func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2020/04/27')

# print(now())
# print(now.__name__)


def log(text):
    # 带有参数
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2020/04/27')

# print(now())
# print(now.__name__)


import time,functools
def metric(fn):
    # 返回函数运行时间
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        fn(*args, **kw)
        end = time.time() -start
        print('%s executed in %.3f ms' %(fn.__name__,end*1000))
        return fn(*args, **kw)
    return wrapper

# 测试
"""
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
"""


def log(fn):
    def decorate(*args, **kw):
        print('begin call %s():' %(fn.__name__,))
        fn(*args, **kw)
        print('end call %s():' %(fn.__name__,))
    return decorate()


@log
def now():
    print('2020/04/27')

# print(now)


import functools

def log(argv):
    # 既支持带参数，也支持不带参数
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('This is decorator')
            if type(argv) == str:
                print('show %s' % argv)
            return func(*args, **kw)
        return wrapper
    if type(argv) == str:
        return deco
    else:
        return deco(argv)

@log
def f():
    print('do f')

@log('execute')
def f1():
    print('do f1')

print(f())
print(f1())
