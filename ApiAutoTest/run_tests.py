import datetime
import os
import smtplib
import sys
import time
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sys.path.append('./interface_scripts')  # 运行时，将目录添加至系统环境变量下，让python解析器解析
sys.path.append('./db_operations')
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_operations import api_test_datas
import sendmail

# 指定测试用例为当前文件夹下的 interface 目录,指定interface目录下的所有_test.py文件
test_dir = './interface_scripts'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

base_dir = str(os.path.dirname(os.path.abspath(__file__)))
base_dir = base_dir.replace('\\', '/')
# report_path = base_dir + '/report/'  # 得到report路径 本地调试使用

if __name__ == "__main__":
    # api_test_datas.init_data()  # 初始化接口测试数据
    now = time.strftime("%Y-%m-%d %H_%M_%S")  # 获取当前时间
    build_number1 = str(os.getenv("BUILD_NUMBER"))#jenkins构建使用
    # build_number1 = '2'#本地调试使用
    path = './report/'+build_number1
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs('./report/' + build_number1)
    report_path = path + '/'
    # filename = path+'/'+now + '_result.html'  # 测试报告名称
    filename = path + '/' + 'hive_api_autotest_report.html'  # 测试报告名称  本地调试+使用
    fp = open(filename, 'wb')  # 以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
    runner = HTMLTestRunner(stream=fp,
                            title='启元项目接口测试报告',
                            description='请在浏览器中打开附件查看详细执行结果 ')
    runner.run(discover)  # 执行测试，结果写入测试报告jenkins
    fp.close()  # 关闭文件
    print('basdir'+base_dir)
    print('report路径：'+report_path)
    sendmail.SENDMAIL().sendreport(report_path)


