# -*- coding:utf-8 -*-
#@Time    : 2019/9/27 16:33
#@Author  : NewDragon
#@Email   : zhongxinlong@bbdservice.com
#@File    : Login_test.py
#@Software: PyCharm

import string
import unittest
import requests
import os, sys
import json
import random
import time
import constants
from utils import rw_excel, requests_beehive, reuse_methods
from utils.reuse_methods import REUSEMETHODS
from utils import pd_excel
import ddt

i = str(random.randint(0, 9999))
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_operations import api_test_datas
from db_operations import mysql_operations

# 读取到对应的sheet页
sheet_name = 'register'
pandas_data = pd_excel.read_excel(sheet_name)

@ddt.ddt
class Register(unittest.TestCase):
    ''' 用户注册接口 '''

    def setUp(self):
        self.headers = {"Content-Type":"application/json"}
        # self.headers['cookie'] = "ssoToken="+reuse_methods.REUSEMETHODS().base_login()['data']['ssoToken']

    def tearDown(self):
        # 清除任务表中的数据
        #reuse_methods.REUSEMETHODS.updateTabelData(self, db_name='qy_listed_dev', tableName='sys_user',organization='小小米科技有限责任公司', user_name='change02')
        pass

    @ddt.data(*pandas_data)
    def test_register(self,data):
        ''' {0} '''.format(data['Name'])

        rq = requests_beehive.REQUESTS_BEEHIVE()  # requests方法

        rr = rq.requests_beehive(data['Method'], data['Url'], json.dumps(eval(data['Data'])),headers=self.headers)  # 执行请求返回数据

        self.result = rr.json()
        print ("self.result:",self.result)
        # 根据result进行断言
        reusem = reuse_methods.REUSEMETHODS()

        reusem.beehiveAssertion(keyName='success', result=self.result, response=eval(data['Response']))
        reusem.beehiveAssertion(keyName='message', result=self.result, response=eval(data['Response']))

        # 根据数据库查询结果与返回结果进行断言
        # sql = "select * from task;"
        # dataPra = json.loads(rwdatas['Data'])
        # # print(type(dataPra))
        # reusem.sqlResultAssertEqual(sql=sql, db_name='auto_spider',keyName='task_type', data=dataPra)

        print(self.result)
        print ("-----------*******------------")



if __name__ == '__main__':
    # api_test_datas.init_data()  # 初始化接口测试数据
    unittest.main()