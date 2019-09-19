#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 14:00
# @Author  : chenjinlin
# @Email   : chenjinlin@bbdservice.com
# @File    : mysql_operations.py
# @Software: PyCharm

import pymysql.cursors
import os
import configparser as cparser
from utils import reuse_methods

# ======== Reading db_config.ini setting ===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"  # 得到db_config.ini文件路径

cf = cparser.ConfigParser()

cf.read(file_path)  # 读取配置文件，分别读取各变量的值
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
# db_name = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


# ======== MySql base operating ===================
class DB:
    # 连接到数据库
    def __init__(self,db_name=''):
        try:
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db_name,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # 清除table_name中的数据
    def clear(self, db_name,table_name):
        DB.__init__(self,db_name)
        # real_sql = "truncate table " + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    # 向table_name插入数据
    def insert(self, db_name,table_name, table_data):
        DB.__init__(self,db_name)
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()

    # 查询table_name返回特定字段的值
    def query(self,db_name,sql,sqlField):
        DB.__init__(self, db_name)
        # real_sql = "select * from " + tabale_name+ " where "+condition+";"
        real_sql = sql
        print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            results = cursor.fetchall()#获取所有查询结果
            # print(type(results))
            # print(results)
            reusem = reuse_methods.REUSEMETHODS()
            field_value = reusem.get_target_value(key=sqlField,dic_tmp=results,data_list=[])#获取特定字段的值写入列表
            # print(type(field_value))
            # print(field_value)
            # print(field_value[0])
        self.connection.commit()
        return field_value

    # 删除table表中的特定行(依据id 或 nid来操作)
    def delete(self, db_name, table_name, id,num):
        DB.__init__(self, db_name)
        # real_sql = "select * from " + tabale_name+ " where "+condition+";"
        # select * from timer where id = 6

        # DELETE * FROM TABLE where id = 1

        real_sql = "DELETE FROM {tablename} where {id} = {num};"
        real_sql = real_sql.format(tablename=table_name,id=id,num=num)

        # print (real_sql)
        with self.connection.cursor() as cursor:
            # cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    # 删除table表中的特定行(依据type来操作)
    def delete_systemconfig(self):
        DB.__init__(self, 'auto_basic')
        # real_sql = "select * from " + tabale_name+ " where "+condition+";"
        # select * from timer where id = 6

        # DELETE * FROM TABLE where id = 1

        real_sql = "DELETE FROM `basic_config` where config_type = 'old';"

        print (real_sql)

        with self.connection.cursor() as cursor:
            # cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    #删除table中的部分数据
    def delete_partialLineDate(self,db_name,table_name,field_title,reserved_fields):
        DB.__init__(self,db_name)
        real_sql = "DELETE FROM "+table_name+" WHERE "+field_title+" NOT IN "+reserved_fields+";"
        # print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")#关闭外键约束
            cursor.execute(real_sql)
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")#打开外键约束
        self.connection.commit()

    # 更新表中的某一行数据
    def update(self, db_name, table_name,organization,user_name):
        DB.__init__(self, db_name)

        real_sql = "UPDATE {tableName} SET organization='{organization}' where username='{userName}';"
        real_sql = real_sql.format(tableName=table_name,organization=organization,userName=user_name)

        print ('real_sql',real_sql)
        with self.connection.cursor() as cursor:
            # cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()


    # 关闭数据库连接
    def close(self):
        self.connection.close()

    # 初始化数据
    def init_data(self, tabale_name):
        # for table, data in datas.items():
        #     self.clear(table)
        #     for d in data:
        #         self.insert(table, d)
        # self.close()
        self.__init__()
        self.clear(self.tabale_name)
        self.close()


if __name__ == '__main__':
    # db = DB()
    # db_name = 'auto_spider'
    # table_name = "task_project"
    # field = 'project_name'
    # sql = "select * from task_project;"
    # data = {'project_id':'32','project_name':'testprojectapi','project_status':'101'}
    #
    # db.clear(table_name)
    # db.insert(table_name, data)
    # sqlvalue = db.query(db_name=db_name,sql=sql,sqlField=field)  # print(sql_result)
    # print(sqlvalue)
    # db.close()
    pass
