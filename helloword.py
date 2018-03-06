# coding:utf8

from soaplib.service import rpc
from soaplib.service import DefinitionBase
from soaplib.serializers.primitive import String, Integer

from soaplib.wsgi import Application
from soaplib.serializers.clazz import Array

import os
import re
import sys


''''' 
This is a simple HelloWorld example to show the basics of writing 
a webservice using soaplib, starting a server, and creating a service 
client. 
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
			<wjm>11001901120180305000008.xml</wjm>
		</QueryCondition>
		<QueryCondition>
			<wjm>11001901120180305000010.xml</wjm>
		</QueryCondition>
		<QueryCondition>
			<wjm>09000109120171123000004.xml</wjm>
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
                                    <root><head>1<code></code><msg>u"数据查询成功"</msg></head>
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
                                    <root><head>1<code></code><msg>u"数据查询成功"</msg></head>
                                                    <body>{file_content}</body></root>"""

        a = ''
        for file_data in return_file_list:
            a += """<result><ywcode>1</ywcode><ywmsg>u"查询成功"</ywmsg><dataObj><wjm>{file_name}</wjm><wjzt>{file_status}</wjzt></dataObj></result>""".format(
                                                                                     file_name=file_data['file_name'],
                                                                                     file_status=file_data[
                                                                                         'file_status'])
        data = return_code.format(file_content=a)

        return data


if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server

        server = make_server('0.0.0.0', 7789, Application([HelloWorldService], 'tns'))
        server.serve_forever()
        print 'listening on 127.0.0.1:7789'
        print 'wsdl is at: http://localhost:7789/SOAP/?wsdl'
    except ImportError:
        print "Error: example server code requires Python >= 2.5"