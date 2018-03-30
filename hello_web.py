# coding:utf-8

from soaplib.service import DefinitionBase
from soaplib.service import rpc
from soaplib.serializers.primitive import String, Integer
from soaplib.serializers.clazz import Array
from soaplib.wsgi import Application

import os
import re
import sys
import datetime
import logging


# class HelloWorldService(DefinitionBase):
#     @rpc(String,Integer,_returns=Array(String))
#     def say_hello(self,name,times):
#         results = []
#         for i in range(0,times):
#             results.append('Hello, %s'%name)
#         return results

def get_file_name(file_full_name):
    return os.path.splitext(file_full_name)[0]


class HelloWorldService(DefinitionBase):
    @rpc(String, _returns=String)
    def get_file_status(self, name):
        '''''
Docstrings for service methods appear as documentation in the wsdl
<b>what fun</b>
@param data the data to say hello to
@param the number of times to say hello
@return the completed array
hello world

>>> from suds.client import Client
>>> hello_client = Client('http://40.125.204.79:7789/content-root/services/SafeOutAccess?wsdl')
>>> result = hello_client.service.get_file_status(
"""<?xml version="1.0" encoding="UTF-8" ?>
<root>
		<QueryCondition>
			<wjm>11001901120180305000008</wjm>
		</QueryCondition>
		<QueryCondition>
			<wjm>11001901120180305000010</wjm>
		</QueryCondition>
		<QueryCondition>
			<wjm>09000109120171123000004</wjm>
		</QueryCondition>
</root>""")
>>> print result
'''
        # results = []
        # for i in range(0, times):
        #     results.append('Hello, %s' % name)
        # return results
        file_list = re.findall('<wjm>(.*?)</wjm>', name)
        file_num = len(file_list)
        if not file_num:
            return """<?xml version="1.0" encoding="UTF-8" ?>
                                    <root><head><code>1</code><msg>u"数据查询成功"</msg></head>
                                                    <body><result><ywcode>0</ywcode><ywmsg>无数据</ywmsg></result></body></root>"""
        file_name_list = map(get_file_name, file_list)
        pre_file_list = os.listdir('/data/xml/pre')
        updated_file_list = os.listdir('/data/xml/uploaded')
        back_file_list = os.listdir('/data/xml/back')

        # 采集文件
        pre_file_name_ist = map(get_file_name, pre_file_list)
        # 上传文件
        update_file_name_list = map(get_file_name, updated_file_list)
        # 本分文件
        back_file_name_list = map(get_file_name, back_file_list)

        return_file_list = []

        # 根据文件名去文件夹下查找文件
        for file_name in file_name_list:
            if file_name not in back_file_name_list:
                if file_name in update_file_name_list:
                    return_file_list.append({"file_status": 4, "file_name": file_name})
                else:
                    return_file_list.append({"file_status": 5, "file_name": file_name})

        return_code = """<?xml version="1.0" encoding="UTF-8" ?>
                                    <root><head><code>1</code><msg>u"数据查询成功"</msg></head>
                                                    <body>{file_content}</body></root>"""

        a = ''
        for file_data in return_file_list:
            a += """<result><ywcode>1</ywcode><ywmsg>u"查询成功"</ywmsg><dataObj><wjm>{file_name}</wjm><wjzt>{file_status}</wjzt></dataObj></result>""".format(
                                                                                     file_name=file_data['file_name'],
                                                                                     file_status=file_data[
                                                                                         'file_status'])
        data = return_code.format(file_content=a)

        return data

    @rpc(String, _returns=String)
    def get_tactrcs_config(self, name):
        """
        全局参数查询
        :param xtlb
        :param jkid
        :param UTF8XmlDoc
        :return:
        """


        return """<?xml version="1.0" encoding="UTF-8"?>
            <root><head><code>1</code><msg>null</msg</head><body><result>
            <ywcode>1</ywcode><ywmsg>u"数据查询成功"</ywmsg>

            <dataObj><gjz>CLSJKZDZ</gjz><csmc>u"存量数据单个数据块最大数据量"</csmc><mrz>10000</mrz></dataObj>
            <dataObj><gjz>CLSJKLJZDZ</gjz><csmc>u"存量数据采集任务最大数据库连接数"</csmc><mrz>20</mrz></dataObj>
            <dataObj><gjz>CLRWQDSJ</gjz><csmc>u"存量数据采集任务启动时间"</csmc><mrz>17</mrz></dataObj>
            <dataObj><gjz>CLRWJSSJ</gjz><csmc>u"存量数据采集任务结束时间"</csmc><mrz>24</mrz></dataObj>
            <dataObj><gjz>ZLCJZQ</gjz><csmc>u"增量数据采集周期"</csmc><mrz>20</mrz></dataObj>
            <dataObj><gjz>RZJXWJZDZ</gjz><csmc>u"日志解析文件最大值"</csmc><mrz>20</mrz></dataObj>
            <dataObj><gjz>FSCSXY</gjz><csmc>u"传输协议NFS、SMB、FTP"</csmc><mrz>NFS</mrz></dataObj>
            <dataObj><gjz>FSUSER</gjz><csmc>u"用户名"</csmc><mrz></mrz></dataObj>
            <dataObj><gjz>FSUSERPASS</gjz><csmc>u"密码"</csmc><mrz></mrz></dataObj>
            <dataObj><gjz>FSIP</gjz><csmc>u"ip地址"</csmc><mrz></mrz></dataObj>
            <dataObj><gjz>FSPORT</gjz><csmc>u"端口号"</csmc><mrz></mrz></dataObj>
            <dataObj><gjz>CLSCML</gjz><csmc>u"文件系统存量文件目录"</csmc><mrz>/share/olddir/</mrz></dataObj>
            <dataObj><gjz>ZLSCML</gjz><csmc>u"文件系统增量文件目录"</csmc><mrz>/share/newdir</mrz></dataObj>
            <dataObj><gjz>JGXTLB</gjz><csmc>u"交管信息系统类别"</csmc><mrz>8010#80综合应用平台,8021#80综合查询系统,8050#80互联网服务平台,8060#80集成指挥平台</mrz></dataObj>
            </result></body></root>"""


if __name__=='__main__':
    try:
        from wsgiref.simple_server import make_server
        server = make_server('localhost', 7790, Application([HelloWorldService], 'tns'))
        server.serve_forever()
    except ImportError:
        print "Error: example server code requires Python >= 2.5"