#!/usr/bin/python
# -*- coding: utf-8 -*-
def by_name(t):
    # 对一组tuple按名字进行排序
    return t[0].lower()

def by_score(t):
    # 对一组tuple按分数进行排序
    return t[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L1 = sorted(L,key=by_name)
L2 = sorted(L,key=by_score,reverse=True)
print('按名字进行排序',L1)
print('按分数进行排序',L2)