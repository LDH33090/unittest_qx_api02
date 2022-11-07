# -*- coding: utf-8 -*-

# 用例  ID: 
# 用例标题: 
# 预置条件:
# 测试步骤:
#    1.公共日志类 2.导入logging库 3.创建日志控制台输出，输出日志到文本记录
# 预期结果:
#    1.控制台可以看到格式化日志后的输出内容
#    2.记录日志的文本，有日志内容写入
# 脚本作者: 林德浩
# 写作日期: 2022/11/2 14:01
import logging
import os.path


class LogCommon:
    logs_dir = os.path.abspath(os.path.join(os.getcwd(), "../logs"))
    logs_path = os.path.join(logs_dir, 'qx.logs')

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    format_str = f'[%(filename)s] [%(asctime)s] [%(levelname)s] [line: %(lineno)d] : [%(message)s]'

    def __init__(self):
        self.format_end = logging.Formatter(self.format_str)

        self.console()
        self.file_input()

    # 定义输出到控制台显示日志的方法
    def console(self):
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)
        consoleHandler.setFormatter(self.format_end)
        self.logger.addHandler(consoleHandler)

    # 定义日志写入到文本内容显示的方法
    def file_input(self):
        if not os.path.exists(self.logs_dir):
            os.mkdir(self.logs_dir)
        fileHandler = logging.FileHandler(filename=self.logs_path, mode='a', encoding='utf-8')
        fileHandler.setLevel(logging.DEBUG)
        fileHandler.setFormatter(self.format_end)
        self.logger.addHandler(fileHandler)

    def console_file_info(self, message):
        return self.logger.info(message)

    def console_file_debug(self, message):
        return self.logger.debug(message)

    def console_file_error(self, message):
        return self.logger.error(message)

    def console_file_warning(self, message):
        return self.logger.warning(message)

    def console_file_critical(self, message):
        return self.logger.critical(message)


"""
DEBUG：程序调试bug时使用
INFO：程序正常运行时使用
WARNING：程序未按预期运行时使用，但并不是错误，如:用户登录密码错误
ERROR：程序出错误时使用，如:IO操作失败
CRITICAL：特别严重的问题，导致程序不能再继续运行时使用，如:磁盘空间为空，一般很少使用

"""

# if __name__ == '__main__':
#     print(LogCommon.logs_dir)
#     print(LogCommon.logs_path)
#     print(LogCommon.console_file('你好啊'))
