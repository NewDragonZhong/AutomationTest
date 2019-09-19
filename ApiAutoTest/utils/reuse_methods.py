#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 9:43
# @Author  : chenjinlin && NewDragon
# @Email   : chenjinlin@bbdservice.com && zhongxinlong@bbdservice.com
# @File    : reuse_methods.py
# @Software: PyCharm
import unittest

import paramiko
import requests
import json

import time

import constants
from db_operations import mysql_operations
from utils import rw_excel
import utils.log as log
from utils import requests_beehive

logging = log.get_logger()


class REUSEMETHODS(unittest.TestCase):
	# 遍历嵌套的字典、列表、元组

	def base_login(self):
		''' 启元登陆接口-正常登陆 '''
		# 获取excel中的行数据
		rwdatas = REUSEMETHODS.getExcelRowByN(self, n='2')  # 项目名称正确

		# 执行请求返回数据
		rq = requests_beehive.REQUESTS_BEEHIVE()
		rr = rq.requests_beehive(rwdatas['Method'], rwdatas['Url'], json.dumps(eval(rwdatas['Data'])))
		self.result = rr.json()

		# 根据result进行断言
		reusem = REUSEMETHODS()
		reusem.beehiveAssertion(keyName='message', result=self.result, response=eval(rwdatas['Response']))
		reusem.beehiveAssertion(keyName='statusCode', result=self.result, response=eval(rwdatas['Response']))
		return self.result

	def get_target_value(self, key, dic_tmp, data_list=[]):
		# data_list = [] #空列表用于存放取出key的数据
		if isinstance(dic_tmp, (dict)):  # 判断传入的数据的类型是字典则执行
			if key in dic_tmp:  # 判断key是否在传入数据中存在
				# 若key在dic_tmp中存在，则添加到data_list列表
				# data_list.append(key)status
				data_list.append(dic_tmp[key])
			else:
				for value in dic_tmp.values():
					if isinstance(value, dict):
						self.get_target_value(key, value, data_list)
					elif isinstance(value, (list, tuple)):
						self._get_value(key, value, data_list)
		elif isinstance(dic_tmp, (list, tuple)):  # 判断传入的数据的类型是列表、元组则执行
			self._get_value(key, dic_tmp, data_list)

		# print (data_list)
		return data_list

	def _get_value(self, key, value, data_list):
		for val_ in value:
			if isinstance(val_, dict):
				self.get_target_value(key, val_, data_list)  # 传入数据的value值是字典，则调用get_target_value
			elif isinstance(val_, (list, tuple)):
				self._get_value(key, val_, data_list)  # 传入数据的value值是列表或者元组，则调用自身

	def beehiveAssertion(self, keyName, result, response):

		reusem = REUSEMETHODS()
		resultkeyValue = reusem.get_target_value(key=keyName, dic_tmp=result, data_list=[])
		responsekeyValue = reusem.get_target_value(key=keyName, dic_tmp=response, data_list=[])
		# print(responsekeyValue,resultkeyValue)
		if responsekeyValue:
			self.assertEqual(resultkeyValue[0], responsekeyValue[0])  # 接口返回数据与excel中用例数据对比
			print('断言成功，' + keyName + ':' + str(resultkeyValue[0]) + '=' + keyName + ':' + str(responsekeyValue[0]))
		else:
			self.assertEqual(resultkeyValue, responsekeyValue)  # 接口返回数据与excel中用例数据对比
			print('断言成功，' + keyName + ':' + str(resultkeyValue) + '=' + keyName + ':' + str(responsekeyValue))

	def sqlResultAssertNotEqual(self, db_name, sql, keyName, data):
		'''2个值不能相等，若相等则断言失败'''

		sqlvalue = mysql_operations.DB().query(db_name, sql, sqlField=keyName)  # 按字段名称查询数据库返回的数据
		reusem = REUSEMETHODS()
		inactDataValue = reusem.get_target_value(key=keyName, dic_tmp=data, data_list=[])  # 实际请求参数值
		# print(inactDataValue)
		if sqlvalue:
			if sqlvalue == inactDataValue:
				self.assertFalse(True, msg='断言失败，不符合需求的数据:“' + str(sqlvalue[0]) + '”，被插入了数据库')
			else:
				print('断言成功，不符合需求的数据，未被插入数据库；' + '数据库查询字段：' + keyName + '=' + str(sqlvalue))
			# raise Exception('断言失败，不符合需求的数据:'+sqlvalue[0]+'，被插入了数据库')#数据不为None则抛出异常
		else:
			self.assertEqual(sqlvalue, [])  # 数据为空，断言成功
			print('断言成功，不符合需求的数据，未被插入数据库；' + '数据库查询字段：' + keyName + '=' + str(sqlvalue))

	# def sqlResultAssertNone(self, sql, keyName, data):
	#     '''数据库查询结果为空断言成功，不为空断言失败'''
	#     sqlvalue = mysql_operations.DB().query(sql, sqlField=keyName)  # 按字段名称查询数据库返回的数据
	#     if sqlvalue :
	#         self.assertFalse(True,msg='断言失败，不符合需求的数据:“'+sqlvalue[0]+'”，被插入了数据库')
	#         # raise Exception('断言失败，不符合需求的数据:'+sqlvalue[0]+'，被插入了数据库')#数据不为None则抛出异常
	#     else:
	#         self.assertEqual(sqlvalue,[])#数据为空，断言成功
	#         print ('断言成功，不符合需求的数据，未被插入数据库；' +'数据库查询字段：'+keyName+'='+str(sqlvalue))


	def sqlResultAssertEqual(self, db_name, sql, keyName, data):
		'''2个值相等，则断言成功'''

		sqlvalue = mysql_operations.DB().query(db_name, sql, sqlField=keyName)  # 按字段名称查询数据库返回的数据
		print('sqlvalue:', sqlvalue)
		if sqlvalue == []:
			sqlvalue = ['']
		print('sqlvalue:', sqlvalue)
		reusem = REUSEMETHODS()
		inactDataValue = reusem.get_target_value(key=keyName, dic_tmp=data, data_list=[])  # 实际请求参数值
		print('inactDataValue:', inactDataValue)
		self.assertEqual(inactDataValue, sqlvalue)  # 数据库查询结果与excel中数据对比
		# print('断言成功，' + keyName + ':' + str(sqlvalue[0]) + '=' + keyName + ':' + str(inactDataValue[0]))
		print('断言成功，' + keyName + ':' + str(sqlvalue) + '=' + keyName + ':' + str(inactDataValue))


	def getExcelRowByN(self, n):
		# 获取excel中的第n行数据
		rw = rw_excel.RW_EXCEL()
		filename = constants.CONSTANTS().FILE_NAME
		sheetname = 'automationApiTestCase'
		m = n  # 接口用例所在行
		rwdatas = rw.getRowValue(filename, sheetname, m)
		return rwdatas

	def clearTableData(self, db_name, tableName):
		# 清空数据
		db = mysql_operations.DB
		# db.__init__(self,db_name)
		db.clear(self, db_name, table_name=tableName)
		db.close(self)

	def insertTableData(self, db_name, tableName, insertData):
		# 插入数据
		db = mysql_operations.DB
		# db.__init__(self,db_name)
		# insert_data = {'project_name': '新增项目接口', 'project_status': '101', 'updated_at': '2018-05-08 16:09:55'}
		db.insert(self, db_name, table_name=tableName, table_data=insertData)
		db.close(self)

	def delete_partialLineDate(self, db_name, table_name, field_title, reserved_fields):
		# 删除数据，保留部分数据，field_title：根据字段删除，reserved_fields：保留特定字段所在行的数据
		db = mysql_operations.DB
		db.delete_partialLineDate(self, db_name, table_name, field_title, str(reserved_fields))
		db.close(self)

	def updateTabelData(self,db_name, tableName,organization,user_name):
		db = mysql_operations.DB
		# db.__init__(self,db_name)
		# insert_data = {'project_name': '新增项目接口', 'project_status': '101', 'updated_at': '2018-05-08 16:09:55'}
		db.update(self, db_name=db_name, table_name=tableName, organization=organization,user_name=user_name)
		db.close(self)

	def python3_ssh(self, ip, port, username, password, lcmds):
		'''rancher环境变量检查-AutoTest-Auto-Web-1_env '''
		try:
			# 创建ssh客户端
			ssh = paramiko.SSHClient()
			ssh.load_system_host_keys()
			# 第一次ssh远程登录提示输入yes或者no
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			# 密码方式远程连接
			ssh.connect(ip, int(port), username, password, timeout=20)
			# ssh.connect(ip, port, username, password, timeout=20,allow_agent=False,look_for_keys=False)
			# 互信方式远程连接
			# key_file = paramiko.RSAKey.from_private_key_file("/root/.ssh/id_rsa")
			# ssh.connect(sys_ip, 22, username=username, pkey=key_file, timeout=20)
			# 执行linux命令
			# stdin, stdout, stderr = ssh.exec_command(lcmds,get_pty=True)
			stdin, stdout, stderr = ssh.exec_command('sudo -S %s\n' % lcmds, get_pty=True)
			# stdin.write('%s\n' % password)
			# stdin.flush()
			# 输出命令执行结果,返回的数据是一个list
			# out = stdout.readlines()
			env_out_list = []
			for i in stdout.read().splitlines():
				env_out_list.append(i.decode('utf-8'))

			# 去掉换行符号
			# for line in out:
			# line = line.rstrip("\r\n")
			# print(line)
			# out = stdout.read()
			# print(stderr)
			# print(env_out_list)
			return env_out_list
			ssh.close()
		except Exception as e:
			# print(e)
			pass

	def python3_ssh_root(self, ip, port, username, password, cmds):
		s = paramiko.SSHClient()
		s.load_system_host_keys()
		s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		s.connect(hostname=ip, port=int(port), username=username, password=password)
		if username != 'root':
			ssh = s.invoke_shell()
			time.sleep(0.1)
			ssh.send('su - \n')
			buff = ''
			while not buff.endswith('Password: '):
				resp = ssh.recv(9999)
				buff += resp.decode()
			ssh.send(password)
			ssh.send('\n')
			buff = ''
			while not buff.endswith('# '):
				resp = ssh.recv(9999)
				buff += resp.decode()
			ssh.send(cmds)
			ssh.send('\n')
			buff = ''
			while not buff.endswith('# '):
				resp = ssh.recv(9999)
				buff += resp.decode()
			s.close()
			result = buff
		else:
			stdin, stdout, stderr = s.exec_command(cmds)
			result = stdout.read()
			s.close()
		return result


if __name__ == '__main__':
	# reusem = REUSEMETHODS()
	unittest.main()
#
# test_dic = {'a': '1', 'b': '2', 'c': {
#     'd': [{'e': [{'f': [{'v': [{'g': '6'}, [{'g': '7'}, [{'g': 8}]]]}, 'm']}]}, 'h', {'g': [10, 12]}]}}
# avalue = reusem.get_target_value(key='a', dic_tmp=test_dic, data_list=[])
# print (avalue)
