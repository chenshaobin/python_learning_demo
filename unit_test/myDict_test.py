#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from unit_test.myDict import Dict

class TestMyDict(unittest.TestCase):
    # 该测试类从unittest.TestCase继承
    # 以test开头的方法就是测试方法，
    # 不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
    # setUp()和tearDown()这两个特殊的方法会分别在每调用一个测试方法的前后分别被执行

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        # 通过d['empty']访问不存在的key,断言抛出KeyError
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        # 通过d.empty访问不存在的key时，断言抛出AttributeError
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()
