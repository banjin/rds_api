# coding:utf8

from soaplib.service import rpc
from soaplib.service import DefinitionBase
from soaplib.serializers.primitive import String, Integer

from soaplib.wsgi import Application
from soaplib.serializers.clazz import Array

import os
import re
import sys
import datetime


''''' 
This is a simple HelloWorld example to show the basics of writing 
a webservice using soaplib, starting a server, and creating a service 
client. 
参考:https://www.jianshu.com/p/ad3c27d2a946
http://blog.sina.com.cn/s/blog_978a39e401016fzg.html
'''


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
    def get_tactrcs_config(self, global_config):
        return """<?xml version="1.0" encoding="UTF-8"?>
        <root><head><code></code><msg>u"数据查询成功"</msg</head><body><result>
        <ywcode>1</ywcode><ywmsg>u"数据查询成功"</ywmsg>
        <dataObj><giz>AZDM</giz><csmc>u"安管系统安装代码"</csmc><mrz>110001</mrz></dataObj>
        <dataObj><giz>CLSJKZDZ</giz><csmc>u"存量数据单个数据块最大数据量"</csmc><mrz>10000</mrz></dataObj>
        <dataObj><giz>CLSJKLJZDZ</giz><csmc>u"存量数据采集任务最大数据库连接数"</csmc><mrz>20</mrz></dataObj>
        <dataObj><giz>CLRWQDSJ</giz><csmc>u"存量数据采集任务启动时间"</csmc><mrz>19</mrz></dataObj>
        <dataObj><giz>CLRWJSSJ</giz><csmc>u"存量数据采集任务结束时间"</csmc><mrz>7</mrz></dataObj>
        <dataObj><giz>ZLCJZQ</giz><csmc>u"增量数据采集周期"</csmc><mrz>1</mrz></dataObj>
        <dataObj><giz>RZJXWJZDZ</giz><csmc>u"日志解析文件最大值"</csmc><mrz>10</mrz></dataObj>
        <dataObj><giz>CLSCML</giz><csmc>u"存量数据文件上传目录"</csmc><mrz>/</mrz></dataObj>
        <dataObj><giz>ZLSCM</giz><csmc>u"增量数据文件上传目录"</csmc><mrz>/</mrz></dataObj>
        <dataObj><giz>JGXTLB</giz><csmc>u"交管信息系统类别"</csmc><mrz>u"01#类别1名称,02#类别2名称"</mrz></dataObj>
        </result></body></root>"""

    @rpc(String, _returns=String)
    def get_single_config(self, single_config):
        now = datetime.datetime.now()
        create_time = now.strftime("%Y-%m-%d %H:%M:%S")
        update_time = now.strftime("%Y-%m-%d %H:%M:%S")

        return """<?xml version="1.0" encoding="UTF-8"?>
            <root><head><code></code><msg>u"数据查询成功"</msg</head><body><result>
            <ywcode>1</ywcode><ywmsg>u"数据查询成功"</ywmsg>
            <dataObj><giz>JGXTLB</giz><csmc>u"系统类别代码"</csmc><mrz>01</mrz></dataObj>
            <dataObj><giz>BM</giz><csmc>u"表名"</csmc><mrz>usera.table01</mrz></dataObj>
            <dataObj><giz>BMMS</giz><csmc>u"表名描述"</csmc><mrz>u"简单的测试数据文件"</mrz></dataObj>
            <dataObj><giz>CLCJBJ</giz><csmc>u"存量数据采集标记"</csmc><mrz>1</mrz></dataObj>
            <dataObj><giz>SJCZD</giz><csmc>u"时间戳字段"</csmc><mrz>starttime</mrz></dataObj>
            <dataObj><giz>CLQSRQ</giz><csmc>u"存量数据起始日期"</csmc><mrz>2017-01-01</mrz></dataObj>
            <dataObj><giz>CLGLTJ</giz><csmc>u"存量数据过滤条件"</csmc><mrz>id&gt1000;id&lt10000</mrz></dataObj>
            <dataObj><giz>CLWCBJ</giz><csmc>u"存量数据采集完成标记"</csmc><mrz>0</mrz></dataObj>
            <dataObj><giz>ZLKHDGLLX</giz><csmc>u"增量数据客户端过滤类型"</csmc><mrz>!sqlplus,PL/SQL Developer</mrz></dataObj>
            <dataObj><giz>ZLINSERT</giz><csmc>u"是否采集'insert'增量数据"</csmc><mrz>1</mrz></dataObj>
            <dataObj><giz>ZLUPDATE</giz><csmc>u"是否采集'update'增量数据"</csmc><mrz>1</mrz></dataObj>
            <dataObj><giz>ZLDELETE</giz><csmc>u"是否采集'delete'增量数据"</csmc><mrz>1</mrz></dataObj>
            <dataObj><giz>CJSJ</giz><csmc>u"策略创建时间"</csmc><mrz>{create_time}</mrz></dataObj>
            <dataObj><giz>GXSJ</giz><csmc>u"策略更新时间"</csmc><mrz>{update_time}</mrz></dataObj>
            </result></body></root>""".format(create_time=create_time, update_time=update_time)


if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server

        server = make_server('0.0.0.0', 7789, Application([HelloWorldService], 'tns'))
        server.serve_forever()
        print 'listening on 127.0.0.1:7789'
        print 'wsdl is at: http://localhost:7789/SOAP/?wsdl'
    except ImportError:
        print "Error: example server code requires Python >= 2.5"
