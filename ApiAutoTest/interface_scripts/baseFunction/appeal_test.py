# -*- coding:utf-8 -*-
#@Time    : 2019/9/30 17:34
#@Author  : NewDragon
#@Email   : zhongxinlong@bbdservice.com
#@File    : appeal_test.py
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



class Appeal(unittest.TestCase):
    ''' 账号申诉接口 '''

    def setUp(self):
        self.headers = {"Content-Type":"application/json"}
        # self.headers['cookie'] = "ssoToken="+reuse_methods.REUSEMETHODS().base_login()['data']['ssoToken']

    def tearDown(self):
        # 清除任务表中的数据
        #reuse_methods.REUSEMETHODS.updateTabelData(self, db_name='qy_listed_dev', tableName='sys_user',organization='小小米科技有限责任公司', user_name='change02')
        pass

    def test_1_appeal(self):
        ''' 账号申诉-正常申诉 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='24')  # 任务名称正确
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

    def test_2_appeal(self):
        ''' 账号申诉-使用重复的用户名 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='25')  # 任务名称正确
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

    def test_3_appeal(self):
        ''' 账号申诉-简单密码 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='26')  # 任务名称正确
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

    def test_4_appeal(self):
        ''' 账号申诉-邮箱格式错误 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='27')  # 任务名称正确
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

    def test_5_appeal(self):
        ''' 账号申诉-手机号码重复 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='28')  # 任务名称正确
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

    def test_6_appeal(self):
        ''' 账号申诉-验证码输入错误 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='29')  # 任务名称正确
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