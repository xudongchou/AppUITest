"""
@project:AppUITest
@author:lenovo
@file:log.py
@ide:PyCharm
@time:2020/9/29 10:42
@month:九月

"""

import logging
import os
class Logger:
        """
        日志方法，调用方法 Logger.logger.info()  Logger.logger.debug()
        赖于模块 logging和os  from helpers import Logger
        :return:
        """
        basedir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_dir="/logs/"
        log_filepath=basedir+log_dir
        logging.basicConfig(level=logging.DEBUG,
                            filename=log_filepath+'output.log',
                            datefmt='%Y/%m/%d %H:%M:%S',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')
        logger = logging.getLogger(__name__)