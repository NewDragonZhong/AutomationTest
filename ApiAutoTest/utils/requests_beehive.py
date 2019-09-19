# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 15:46
# @Author  : NewDragon
# @Email   : zhongxinlong@bbdservice.com
# @File    : requestsPackage.py
# @Software: PyCharm

import requests
import utils.log as log
import json

logging = log.get_logger()

class REQUESTS_BEEHIVE:

    # def change_type(value):
    #     """
    #     对dict类型进行中文识别
    #     :param value: 传的数据值
    #     :return: 转码后的值
    #     """
    #     try:
    #         if isinstance(eval(value), str):
    #             return value
    #         if isinstance(eval(value), dict):
    #             result = eval(json.dumps(value))
    #             return result
    #     except Exception as e:
    #         logging.error("类型问题 %s", e)

    def requests_beehive(self,method, url, data,headers={"Content-Type":"application/json"}):

        ''' 请求方法封装 '''
        session = requests.Session()#用request创建一个session 然后以后用session请求
        r = None

        try:
            if method == ("post" or "POST"):
                r = session.post(url,data,headers=headers)
                session.close()
            elif method == ("get" or "GET"):
                print ("get打印了！")
                r = session.get(url, data)
                session.close()
            elif method == ("put" or "PUT"):
                print ("put打印了！")
                r = session.put(url, data)
                session.close()
            elif method == ("delete" or "DELETE"):
                print ("delete打印了！")
                r = session.delete(url, data)
                session.close()
        except Exception as e:
            logging.error("service is error", e)
        finally:
            return r

if __name__ == '__main__':
    rq = REQUESTS_BEEHIVE()

    # rq.requests_beehive()