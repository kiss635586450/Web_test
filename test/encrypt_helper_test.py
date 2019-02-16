import unittest
from common import encrypt_helper
import datetime
from common import json_helper
import json
class DbHelperTest(unittest.TestCase):
    def setUp(self):
        """初始化测试环境"""
        print('------ini------')

    def tearDown(self):
        """清理测试环境"""
        print('------clear------')
    def test(self):
        dict = {
            'a': 1,
            'b': "2"
        }
        result = encrypt_helper.md5(dict)
        print(result)

        result = encrypt_helper.md5('1')
        print(result)

        result = encrypt_helper.md5(b'1')
        print(result)
    def test1(self):
        js = {
            'test5': datetime.datetime.now()
        }
        print(js)
        result = json.dumps(js, cls=json_helper.CJsonEncoder)
        print(result)

if __name__ == '__main__':
    unittest.main()