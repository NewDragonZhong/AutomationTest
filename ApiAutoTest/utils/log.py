# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 14:28
# @Author  : NewDragon
# @Email   : zhongxinlong@bbdservice.com
# @File    : log.py
# @Software: PyCharm

import logging

def get_logger():
    global logPath
    try:
        logPath
    except NameError:
        logPath = ""
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    return logging