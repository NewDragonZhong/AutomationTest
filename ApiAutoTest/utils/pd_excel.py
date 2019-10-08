# -*- coding:utf-8 -*-
#@Time    : 2019/10/8 9:35
#@Author  : NewDragon
#@Email   : zhongxinlong@bbdservice.com
#@File    : pd_excel.py
#@Software: PyCharm


import pandas as pd


def read_excel(sheet_name):
    path = r'F:\GitHub\ApiAutoTest\automationApiTestCaseData.xlsx'
    df = pd.read_excel(path, sheetname=sheet_name, header=0)
    test_data = []
    for i in df.index.values:  # 获取行号的索引，并对其进行遍历
        # 根据i 来获取每一行指定的数据 并利用to_dict转换成一个字典
        row_data = df.ix[i, ['Name', 'Data', 'Url', 'Method', 'Response']].to_dict()
        test_data.append(row_data)
    return test_data


if __name__ == '__main__':
    sheet_name = 'appeal'

    rr = read_excel(sheet_name)
    print (rr)


