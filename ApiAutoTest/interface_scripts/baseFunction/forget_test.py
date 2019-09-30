# -*- coding:utf-8 -*-
#@Time    : 2019/9/30 17:28
#@Author  : NewDragon
#@Email   : zhongxinlong@bbdservice.com
#@File    : forget_test.py
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

i = str(random.randint(0, 9999))
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_operations import api_test_datas
from db_operations import mysql_operations



class Forget(unittest.TestCase):
    ''' 忘记密码接口 '''

    def setUp(self):
        self.headers = {"Content-Type":"application/json"}
        # self.headers['cookie'] = "ssoToken="+reuse_methods.REUSEMETHODS().base_login()['data']['ssoToken']

    def tearDown(self):
        # 清除任务表中的数据
        #reuse_methods.REUSEMETHODS.updateTabelData(self, db_name='qy_listed_dev', tableName='sys_user',organization='小小米科技有限责任公司', user_name='change02')
        pass

    def test_1_forget(self):
        ''' 忘记密码-正常修改 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='20')  # 任务名称正确
        rq = requests_beehive.REQUESTS_BEEHIVE()  # requests方法

        rr = rq.requests_beehive(rwdatas['Method'], rwdatas['Url'], json.dumps(eval(rwdatas['Data'])),headers=self.headers)  # 执行请求返回数据

        self.result = rr.json()
        print ("self.result:",self.result)
        # 根据result进行断言
        reusem = reuse_methods.REUSEMETHODS()

        reusem.beehiveAssertion(keyName='success', result=self.result, response=eval(rwdatas['Response']))
        reusem.beehiveAssertion(keyName='message', result=self.result, response=eval(rwdatas['Response']))

        # 根据数据库查询结果与返回结果进行断言
        # sql = "select * from task;"
        # dataPra = json.loads(rwdatas['Data'])
        # # print(type(dataPra))
        # reusem.sqlResultAssertEqual(sql=sql, db_name='auto_spider',keyName='task_type', data=dataPra)

        print(self.result)
        print ("-----------*******------------")

    def test_2_forget(self):
        ''' 忘记密码-用户名不存在 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='21')  # 任务名称正确
        rq = requests_beehive.REQUESTS_BEEHIVE()  # requests方法

        rr = rq.requests_beehive(rwdatas['Method'], rwdatas['Url'], json.dumps(eval(rwdatas['Data'])),headers=self.headers)  # 执行请求返回数据

        self.result = rr.json()
        print ("self.result:",self.result)
        # 根据result进行断言
        reusem = reuse_methods.REUSEMETHODS()

        reusem.beehiveAssertion(keyName='success', result=self.result, response=eval(rwdatas['Response']))
        reusem.beehiveAssertion(keyName='message', result=self.result, response=eval(rwdatas['Response']))

        # 根据数据库查询结果与返回结果进行断言
        # sql = "select * from task;"
        # dataPra = json.loads(rwdatas['Data'])
        # # print(type(dataPra))
        # reusem.sqlResultAssertEqual(sql=sql, db_name='auto_spider',keyName='task_type', data=dataPra)

        print(self.result)
        print ("-----------*******------------")

    def test_3_forget(self):
        ''' 忘记密码-手机号码错误 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='22')  # 任务名称正确
        rq = requests_beehive.REQUESTS_BEEHIVE()  # requests方法

        rr = rq.requests_beehive(rwdatas['Method'], rwdatas['Url'], json.dumps(eval(rwdatas['Data'])),headers=self.headers)  # 执行请求返回数据

        self.result = rr.json()
        print ("self.result:",self.result)
        # 根据result进行断言
        reusem = reuse_methods.REUSEMETHODS()

        reusem.beehiveAssertion(keyName='success', result=self.result, response=eval(rwdatas['Response']))
        reusem.beehiveAssertion(keyName='message', result=self.result, response=eval(rwdatas['Response']))

        # 根据数据库查询结果与返回结果进行断言
        # sql = "select * from task;"
        # dataPra = json.loads(rwdatas['Data'])
        # # print(type(dataPra))
        # reusem.sqlResultAssertEqual(sql=sql, db_name='auto_spider',keyName='task_type', data=dataPra)

        print(self.result)
        print ("-----------*******------------")

    def test_4_forget(self):
        ''' 忘记密码-前后密码输入不一致 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='23')  # 任务名称正确
        rq = requests_beehive.REQUESTS_BEEHIVE()  # requests方法

        rr = rq.requests_beehive(rwdatas['Method'], rwdatas['Url'], json.dumps(eval(rwdatas['Data'])),headers=self.headers)  # 执行请求返回数据

        self.result = rr.json()
        print ("self.result:",self.result)
        # 根据result进行断言
        reusem = reuse_methods.REUSEMETHODS()

        reusem.beehiveAssertion(keyName='success', result=self.result, response=eval(rwdatas['Response']))
        reusem.beehiveAssertion(keyName='message', result=self.result, response=eval(rwdatas['Response']))

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