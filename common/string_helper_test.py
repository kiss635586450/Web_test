import unittest
from common import string_helper

# !/usr/bin/evn python
# coding=utf-8

import unittest
from common import string_helper


class StringHelperTest(unittest.TestCase):
    """字符串操作包测试类"""

    def setUp(self):
        """初始化测试环境"""
        print('------ini------')

    def tearDown(self):
        """清理测试环境"""
        print('------clear------')

    def test_is_email(self):
        print(string_helper.is_email('aaaaa'), False)
        print(string_helper.is_email('aaaa@xxx.com'), True)
        print(string_helper.is_email('aaaa@123.com'), True)
        self.assertEqual(string_helper.is_email('xxx@xxx.com.xx'), True)

    def test_is_phone(self):
        self.assertEqual(string_helper.is_phone('aaaaa'), False)
        self.assertEqual(string_helper.is_phone('12345678'), False)
        self.assertEqual(string_helper.is_phone('01012345678'), True)
        self.assertEqual(string_helper.is_phone('010-123456'), False)
        self.assertEqual(string_helper.is_phone('010-12345678'), True)
        self.assertEqual(string_helper.is_phone('010 12345678'), True)
        self.assertEqual(string_helper.is_phone('0757 12345678'), True)

    def test_is_mobile(self):
        self.assertEqual(string_helper.is_mobile('aaaaa'), False)
        self.assertEqual(string_helper.is_mobile('123456789'), False)
        self.assertEqual(string_helper.is_mobile('13012345678'), True)
        self.assertEqual(string_helper.is_mobile('14012345678'), False)

    def test_is_letters(self):
        self.assertEqual(string_helper.is_letters('123456'), False)
        self.assertEqual(string_helper.is_letters('1ds2f12sdf'), False)
        self.assertEqual(string_helper.is_letters('absbdsf'), True)
        self.assertEqual(string_helper.is_letters('ADdfFSds'), True)

    def test_is_idcard(self):
        self.assertEqual(string_helper.is_idcard('123456789'), False)
        self.assertEqual(string_helper.is_idcard('aaaaaaaaa'), False)
        self.assertEqual(string_helper.is_idcard('340223190008210470'), False)
        self.assertEqual(string_helper.is_idcard('34022319000821047X'), True)


if __name__ == '__main__':
    unittest.main()