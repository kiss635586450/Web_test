import logging
import os
import unittest
from common import log_helper

class LogHelperTest(unittest.TestCase):
    """"日志操作包测试"""

    def setUp(self):
        """初始化测试环境"""
        print('------ini------')
        #获取本脚本所在的上级路径（因为log_helper_test.py是在test目录下，并不再
        #根目录，而我们需要将日志记录在根目录下log目录中，所以需要获取test的上级目录 ）
        program_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        #初始化目录
        log_path = os.path.join(program_path, 'log')
        #当日志目录不存在时创建日志目录
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        #定义日志输出格式
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            filename="%s/info.log" % log_path,
                            filemode='a'
                            )

    def tearDown(self):
        """清理测试环境"""
        print('------clear------')
    def test(self):
        log_helper.info('记录代码执行的相关信息或记录')
        try:
            result = '0'/10
        except Exception as e:
            log_helper.error('出现异常' + str(e.args))

if __name__ == '__main__':
    unittest.main()