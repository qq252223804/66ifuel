# coding=utf-8
import logging, time, os
from colorama import Fore, Style

'''创建logger
创建handler
定义formatter
给handler添加formatter
给logger添加handler
'''
# 这个是日志保存本地的路径
log_path = 'C:\\Users\\p\\Desktop\\66ifuel\\log'
if not os.path.exists(log_path):
    os.makedirs(log_path)


class Log:
    # 文件的命名
    #日志按天统计    %Y_%m_%d_%H_%M这个格式会按分钟统计
    logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))

    logger = logging.getLogger()

    # Logger是Logging模块的主体，进行以下三项工作：
    # 1.为程序提供记录日志的接口
    # 2.判断日志所处级别，并判断是否要过滤
    # 3.根据其日志级别将该条日志分发给不同handler

    # 另外你也可以通过日志名称来区分同一程序的不同模块，比如这个例子。
    # self.logger=logging.getLogger('App.ui')
    # self.logger = logging.getLogger('App.service')
    formatter = logging.Formatter('[%(asctime)s]- %(filename)s]- %(levelname)s: %(message)s')
    # 设置日志级别,格式     这里必须设置成DEBUG 不然日志只显示请求host 不显示路径
    #设置成DEBUG 会打印所有请求信息
    logger.setLevel(logging.INFO)

    # 建立一个filehandler来把日志记录在文件里，级别为以上
    fh = logging.FileHandler(logname, 'a', encoding='utf-8')
    fh.setFormatter(formatter)  # 设定的fh应用到日志输出格式中
    logger.addHandler(fh)  # 把filehandler添加到logger主体中

    # 建立一个streamhandler来把日志打在CMD窗口上，级别为debug以上
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)  #
    # 关闭打开的文件
    fh.close()

    # def getlog(cls):
    # 	return cls.logger
    # @classmethod
    def info(cls, message):
        cls.logger.info(Fore.GREEN + message)

    def debug(cls, message):
        cls.logger.debug(Fore.RED + message)

    def warning(cls, message):
        cls.logger.warning(Fore.YELLOW + message)

    #
    def error(self, message):
        self.logger.error(Fore.BLUE + message)


#
# def critical(self, message):
# 	self.logger.critical(message)


if __name__ == "__main__":

    log = Log()
    log.info("一个info信息")
    log.debug("一个debug信息")
    log.warning("一个waring信息")
# log.error('一个error信息')
# log.critical('一个致命critical信息')
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(logging.error('HTTP请求方法错误，请确认[Request Method]字段是否正确！！！'))
