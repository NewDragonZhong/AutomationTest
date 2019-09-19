#!/usr/bin/env python
# -*- coding: utf-8 -*-



import requests
import os
import json


class fileSystem:

    def get_file_info(self,filename):
        path = os.getcwd()

        file_path = os.path.join(path,filename)
        print('文件路径'+file_path)

        f = open(file_path,'rb')
        file = {'file':f}

        return file


    def uploadFile(self,filename,url):
        file = self.get_file_info(filename)
        response = requests.post(url,files=file)

        file['file'].close()

        # print (response.text)

        return response.json()


    def downLoadFile(self,fileName,url):
        response = requests.get(url,data={'filename':fileName,'path':r'upload/'})
        print (response.text)


if __name__ == '__main__':

    fs = fileSystem()
    fs.uploadFile('test.jpg','http://10.28.100.154:48001/spider/system/upload')
    # fs.downLoadFile('test.zip', 'http://10.28.100.154:48001/spider/system/download')
