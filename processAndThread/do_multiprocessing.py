#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os
# 子程序要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))  # 'test'即为子程序的name值
    print('Child process will start')
    p.start()
    p.join()  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')
