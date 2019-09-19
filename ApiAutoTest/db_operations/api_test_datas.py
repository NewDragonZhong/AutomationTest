# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 14:02
# @Author  : chenjinlin
# @Email   : chenjinlin@bbdservice.com
# @File    : api_test_datas.py
# @Software: PyCharm

import sys
sys.path.append('../db_operations')
try:
    from mysql_operations import DB
except ImportError:
    from .mysql_operations import DB



# create data
datas = {
    'task_project':[
        {'project_id': '32', 'project_name': 'testprojectapi', 'project_status': '101'},
        {'project_id': '33', 'project_name': 'testprojectapi', 'project_status': '101'},
    ],
    'task_class':[
        {'class_id':1,'class_name':'class1'},
        {'class_id':2,'class_name':'class2'},
    ],
}


# Inster table datas
def init_data():
    DB().init_data(datas)


if __name__ == '__main__':
    init_data()