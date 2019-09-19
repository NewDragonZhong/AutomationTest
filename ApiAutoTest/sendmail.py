# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 10:07
# @Author  : chenjinlin && NewDragon
# @Email   : chenjinlin@163.com && zhongxinlong@bbdservice.com
# @File    : sendmail.py
# @Software: PyCharm
import time, time, datetime, sys
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import mimetypes
from email.mime.application import MIMEApplication
import email.mime.multipart
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders


# 定义发邮件
class SENDMAIL:
    def sendmail(self, file_new, lists):
        # 发信邮箱
        mail_from = 'zhongxinlong@bbdservice.com'
        # 收信邮箱
        # 收信邮箱
        # to_addr_list = ['fanliang@bbdservice.com']

        to_addr_list = ['zhongxinlong@bbdservice.com',]
        # mail_to = 'fanliang@bbdserviceservice.com'
        mail_to = to_addr_list

        # 定义正文
        f = open(file_new, 'rb')
        mail_body = f.read()
        f.close()

        msg = MIMEMultipart()
        cotent = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg.attach(cotent)
        # 定义标题
        msg['Subject'] = u"启元项目接口测试报告"
        # 添加附件
        ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        file = MIMEBase(maintype, subtype)
        file.set_payload(open(file_new, 'rb').read())
        file.add_header('Content-Disposition', 'attachment', filename=lists[-1])
        encoders.encode_base64(file)
        msg.attach(file)
        # 定义发送时间
        msg['date'] = time.strftime('%a,%d %b %Y %H:%M:%S %z')
        smtp = smtplib.SMTP()
        # 连接SMTP服务器
        smtp.connect('smtp.bbdservice.com')
        # 用户名密码
        smtp.ehlo()
        smtp.starttls()
        smtp.login('zhongxinlong@bbdservice.com', '08123310190zxl')
        smtp.sendmail(mail_from, mail_to, msg.as_string())
        smtp.quit()
        print('邮件已发送')

    # 查找测试报告，调用发邮件功能
    def sendreport(self, report_path):
        result_dir = report_path
        lists = os.listdir(result_dir)
        # lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not
        # os.path.isdir(result_dir + "\\" + fn) else 0)
        lists.sort(key=lambda fn: os.path.getmtime(result_dir + fn) if not
        os.path.isdir(result_dir + fn) else 0)
        print (u'最新测试生成的报告： ' + lists[-1])
        # 找到最新生成的文件
        file_new = os.path.join(result_dir, lists[-1])
        print(file_new)
        # 调用发邮件模块
        self.sendmail(file_new, lists)


if __name__ == "__main__":
    # 执行发邮件
    pass
