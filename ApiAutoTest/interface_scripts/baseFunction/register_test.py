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

i = str(random.randint(0, 9999))
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_operations import api_test_datas
from db_operations import mysql_operations



class Register(unittest.TestCase):
    ''' 用户注册接口 '''

    def setUp(self):
        self.headers = {"Content-Type":"application/json"}
        # self.headers['cookie'] = "ssoToken="+reuse_methods.REUSEMETHODS().base_login()['data']['ssoToken']

    def tearDown(self):
        # 清除任务表中的数据
        #reuse_methods.REUSEMETHODS.updateTabelData(self, db_name='qy_listed_dev', tableName='sys_user',organization='小小米科技有限责任公司', user_name='change02')
        pass

    def test_1_register(self):
        ''' 注册接口-正常注册 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='10')  # 任务名称正确
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

    def test_2_register(self):
        ''' 注册接口-用户名重复 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='11')  # 任务名称正确
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

    def test_3_register(self):
        ''' 注册接口-企业名/统一社会信用代码为空 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='12')  # 任务名称正确
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

    def test_4_register(self):
        ''' 注册接口-姓名为空 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='13')  # 任务名称正确
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

    def test_5_register(self):
        ''' 注册接口-密码前后不一致 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='14')  # 任务名称正确
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

    def test_6_register(self):
        ''' 注册接口-手机号码为空 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='15')  # 任务名称正确
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

    def test_7_register(self):
        ''' 注册接口-手机号码重复 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='16')  # 任务名称正确
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

    def test_8_register(self):
        ''' 注册接口-验证码输入错误 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='17')  # 任务名称正确
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

    def test_9_register(self):
        ''' 注册接口-手机验证码输入错误 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='18')  # 任务名称正确
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

    def test_10_register(self):
        ''' 注册接口-不勾选使用协议 '''
        # 获取excel中的行数据
        rwdatas = reuse_methods.REUSEMETHODS.getExcelRowByN(self, n='19')  # 任务名称正确
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