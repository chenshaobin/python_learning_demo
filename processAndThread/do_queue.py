#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码
def write(q):
    print('Process to write : %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)  # 将value放入队列
    time.sleep(random.random())

# 读数据进程执行的代码
def read(q):
    print('Process to read:%s' % os.getpid())
    while True:
        value = q.get(True)  # 从队列中移除并返回一个项目。如果可选参数 block 是 true 并且 timeout 是 None (默认值)，则在必要时阻塞至项目可得到
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
