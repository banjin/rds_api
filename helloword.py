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
import logging


''''' 
This is a simple HelloWorld example to show the basics of writing 
a webservice using soaplib, starting a server, and creating a service 
client. 
参考:https://www.jianshu.com/p/ad3c27d2a946
http://blog.sina.com.cn/s/blog_978a39e401016fzg.html
'''

logger = logging.getLogger("soap")
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

# 文件日志
file_handler = logging.FileHandler("ag_test.log")
file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

# 为logger添加的日志处理器
logger.addHandler(file_handler)

# 指定日志的最低输出级别，默认为WARN级别
logger.setLevel(logging.INFO)


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
>>> hello_client = Client('http://40.125.204.79:7789/bigweb/services/SafeOutAccess?wsdl')
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

    @rpc(String, Integer, String, _returns=String)
    def get_tactrcs_config(self, xtlb, jkid, UTF8XmlDoc):
        """
        全局参数查询
        :param xtlb:
        :param jkid:
        :param UTF8XmlDoc:
        :return:
        """
        xtlb = xtlb
        jkid = jkid
        doc_string = UTF8XmlDoc

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

    @rpc(String, String, String, _returns=String)
    def get_single_config(self, xtlb, jkid, UTF8XmlDoc):
        """
        单表参数查询
        :param single_config:
        :return:
        """
        now = datetime.datetime.now()
        create_time = now.strftime("%Y-%m-%d %H:%M:%S")
        update_time = now.strftime("%Y-%m-%d %H:%M:%S")

        return """<?xml version="1.0" encoding="UTF-8"?>
            <root><head><code>1</code><msg>null</msg</head><body><result>
            <ywcode>1</ywcode><ywmsg>u"数据查询成功"</ywmsg>
            <dataObj>
            <bm>asd</bm>
            <jgxtlb>21</jgxtlb>
            <bmms>asd</bmms>
            <clcjbj>1</clcjbj>
            <sjczd>sad</sjczd>
            <clqsrq>2017-12-05 00:00:00</clqsrq>
            <clgltj>asda</clgltj>
            <clwcbj></clwcbj>
            <zlkhdgllx>plsqldev</zlkhdgllx>
            <zlinsert>1</zlinsert>
            <zlupdate>1</zlupdate>
            <zldelete>1</zldelete>
            <cjsj>{create_time}</cjsj>
            <gxsj>{update_time}</gxsj>
            </dataObj>
            
            <dataObj>
            <bm>asda</bm>
            <jgxtlb>21</jgxtlb>
            <bmms>sdada</bmms>
            <clcjbj>1</clcjbj>
            <sjczd>asd</sjczd>
            <clqsrq>2017-12-05 00:00:00</clqsrq>
            <clgltj>asd</clgltj>
            <clwcbj></clwcbj>
            <zlkhdgllx>jdbc</zlkhdgllx>
            <zlinsert>1</zlinsert>
            <zlupdate>0</zlupdate>
            <zldelete>1</zldelete>
            <cjsj>{create_time}</cjsj>
            <gxsj>{update_time}</gxsj>
            </dataObj>
            
            <dataObj>
            <bm>czc</bm>
            <jgxtlb>21</jgxtlb>
            <bmms>zczx</bmms>
            <clcjbj>1</clcjbj>
            <sjczd>zxc</sjczd>
            <clqsrq>2017-12-05 00:00:00</clqsrq>
            <clgltj>asa</clgltj>
            <clwcbj></clwcbj>
            <zlkhdgllx>jdbc</zlkhdgllx>
            <zlinsert>0</zlinsert>
            <zlupdate>1</zlupdate>
            <zldelete>0</zldelete>
            <cjsj>{create_time}</cjsj>
            <gxsj>{update_time}</gxsj>
            </dataObj>
            
            <dataObj>
            <bm>vio_serveil</bm>
            <jgxtlb>10</jgxtlb>
            <bmms>u"非现场违法表"</bmms>
            <clcjbj>0</clcjbj>
            <sjczd></sjczd>
            <clqsrq></clqsrq>
            <clgltj></clgltj>
            <clwcbj></clwcbj>
            <zlkhdgllx>plsqldev</zlkhdgllx>
            <zlinsert>1</zlinsert>
            <zlupdate>1</zlupdate>
            <zldelete>0</zldelete>
            <cjsj>{create_time}</cjsj>
            <gxsj>{update_time}</gxsj>
            </dataObj>
            
            <dataObj>
            <bm>111</bm>
            <jgxtlb>10</jgxtlb>
            <bmms>u"测试2"</bmms>
            <clcjbj>1</clcjbj>
            <sjczd>jxsj</sjczd>
            <clqsrq>2017-12-05 00:00:00</clqsrq>
            <clgltj>22222</clgltj>
            <clwcbj></clwcbj>
            <zlkhdgllx>plsqldev</zlkhdgllx>
            <zlinsert>1</zlinsert>
            <zlupdate>1</zlupdate>
            <zldelete>1</zldelete>
            <cjsj>{create_time}</cjsj>
            <gxsj>{update_time}</gxsj>
            </dataObj>
            
            <dataObj>
            <bm>8</bm>
            <jgxtlb>21</jgxtlb>
            <bmms>8</bmms>
            <clcjbj>1</clcjbj>
            <sjczd>8</sjczd>
            <clqsrq>2017-12-05 00:00:00</clqsrq>
            <clgltj></clgltj>
            <clwcbj></clwcbj>
            <zlkhdgllx>plsqldev</zlkhdgllx>
            <zlinsert>0</zlinsert>
            <zlupdate>0</zlupdate>
            <zldelete>0</zldelete>
            <cjsj>{create_time}</cjsj>
            <gxsj>{update_time}</gxsj>
            </dataObj>
            
            </result></body></root>""".format(create_time=create_time, update_time=update_time)


    @rpc(String, String, String, _returns=String)
    def post_jump(self, xtlb, jkid, UTF8XmlDoc):
        """
        心跳状态上报
        :param self:
        :param xtlb:
        :param jkid:
        :param UTF8XmlDoc:
        :return:
        """
        return """
        <?xml version="1.0" encoding="UTF-8"?>
            <root><head><code>1</code><msg>null</msg</head><body><result>
            <ywcode>1</ywcode><ywmsg>u"数据查询成功"</ywmsg></result></body></root>
        """

    @rpc(String, String, String, _returns=String)
    def post_run_status(self, xtlb, jkid, UTF8XmlDoc):
        """
        采集软件运行状态写入
        :param self:
        :param xtlb:
        :param jkid:
        :param UTF8XmlDoc:
        :return:
        """
        pass

    @rpc(String, String, String, _returns=String)
    def post_cl_status(self, xtlb, jkid, UTF8XmlDoc):
        """
        存量数据处理状态写入
        :param self:
        :param xtlb:
        :param jkid:
        :param UTF8XmlDoc:
        :return:
        """
        pass

    @rpc(String, String, String, _returns=String)
    def post_cl_dd(self, xtlb, jkid, UTF8XmlDoc):
        """
        存量数据断点写入
        :param self:
        :param xtlb:
        :param jkid:
        :param UTF8XmlDoc:
        :return:
        """
        pass

    @rpc(String, String, String, _returns=String)
    def post_cl_file_info(self, xtlb, jkid, UTF8XmlDoc):
        """
        存量数据文件信息写入
        :param self:
        :param xtlb:
        :param jkid:
        :param UTF8XmlDoc:
        :return:
        """
        pass

    @rpc(String, String, String, _returns=String)
    def post_zl_dd(self, xtlb, jkid, UTF8XmlDoc):
        """
        增量数据断点写入
        :param self:
        :param xtlb:
        :param jkid:
        :param UTF8XmlDoc:
        :return:
        """
        pass

    @rpc(String, String, String, _returns=String)
    def post_zl_file_info(self, xtlb, jkid, UTF8XmlDoc):
        """
        增量数据文件信息写入
        :param self:
        :param xtlb:
        :param jkid:
        :param UTF8XmlDoc:
        :return:
        """
        pass

    @rpc(String, String, String, _returns=String)
    def post_ddl_file_info(self, xtlb, jkid, UTF8XmlDoc):
        """
        DDL 数据审计信息写入
        :param self:
        :param xtlb:
        :param jkid:
        :param UTF8XmlDoc:
        :return:
        """
        pass

    @rpc(String, String, String, _returns=String)
    def post_total(self, xtlb, jkid, UTF8XmlDoc):
        """
        数据采集情况统计信息写入
        :param self:
        :param xtlb:
        :param jkid:
        :param UTF8XmlDoc:
        :return:
        """
        pass


if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server

        server = make_server('0.0.0.0', 7789, Application([HelloWorldService], 'tns'))
        server.serve_forever()
        print 'listening on 127.0.0.1:7789'
        print 'wsdl is at: http://localhost:7789/SOAP/?wsdl'
    except ImportError:
        print "Error: example server code requires Python >= 2.5"
