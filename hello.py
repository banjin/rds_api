# coding:utf-8

from soaplib.service import rpc
from soaplib.service import DefinitionBase
from soaplib.serializers.primitive import String, Integer

from soaplib.wsgi import Application
from soaplib.serializers.clazz import Array

import os
import re
import sys
import logging
import datetime


''''' 
This is a simple HelloWorld example to show the basics of writing 
a webservice using soaplib, starting a server, and creating a service 
client. 
'''

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

# 文件日志
file_handler = logging.FileHandler("server.log")
file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

# 为logger添加的日志处理器
logger.addHandler(file_handler)

# 指定日志的最低输出级别，默认为WARN级别
logger.setLevel(logging.INFO)


def get_file_name(file_full_name):
    return os.path.splitext(file_full_name)[0]


class HelloWorldService(DefinitionBase):
    @rpc(String, String, String, String, String, String, _returns=String)
    def queryRdsOut(self, xtlb='', jkxlh='', jkid='', babh='', wkmac='', UTF8XmlDoc=''):
        '''''
Docstrings for service methods appear as documentation in the wsdl
<b>what fun</b>
@param data the data to say hello to
@param the number of times to say hello
@return the completed array
hello world
>>> from suds.client import Client
>>> hello_client = Client('http://localhost:7789/?wsdl')
>>> result = hello_client.service.get_file_status("Dave")
>>> print result
'''
        # 全局参数查询
        if jkid == "81Q01":
            logger.info(u"获取全局策略")
            return """<?xml version="1.0" encoding="UTF-8"?><root><head><code>1</code><msg>null</msg></head><body><result><ywcode>1</ywcode><ywmsg>u"数据查询成功"</ywmsg><dataObj><gjz>CLSJKZDZ</gjz><csmc>存量数据单个数据块最大数据量</csmc><mrz>10000</mrz></dataObj><dataObj><gjz>CLSJKLJZDZ</gjz><csmc>存量数据采集任务最大数据库连接数</csmc><mrz>20</mrz></dataObj><dataObj><gjz>CLRWQDSJ</gjz><csmc>存量数据采集任务启动时间</csmc><mrz>01</mrz></dataObj><dataObj><gjz>CLRWJSSJ</gjz><csmc>存量数据采集任务结束时间</csmc><mrz>24</mrz></dataObj><dataObj><gjz>ZLCJZQ</gjz><csmc>增量数据采集周期</csmc><mrz>20</mrz></dataObj><dataObj><gjz>RZJXWJZDZ</gjz><csmc>日志解析文件最大值</csmc><mrz>20</mrz></dataObj><dataObj><gjz>FSCSXY</gjz><csmc>传输协议NFS、SMB、FTP</csmc><mrz>FTP</mrz></dataObj><dataObj><gjz>FSUSER</gjz><csmc>用户名</csmc><mrz>ftpuser5</mrz></dataObj><dataObj><gjz>FSUSERPASS</gjz><csmc>密码</csmc><mrz>123qwe</mrz></dataObj><dataObj><gjz>FSIP</gjz><csmc>ip地址</csmc><mrz>10.0.40.5</mrz></dataObj><dataObj><gjz>FSPORT</gjz><csmc>端口号</csmc><mrz>21</mrz></dataObj><dataObj><gjz>CLSCML</gjz><csmc>文件系统存量文件目录</csmc><mrz>/share/olddir/</mrz></dataObj><dataObj><gjz>ZLSCML</gjz><csmc>文件系统增量文件目录</csmc><mrz>/share/newdir</mrz></dataObj><dataObj><gjz>JGXTLB</gjz><csmc>交管信息系统类别</csmc><mrz>8010#80综合应用平台,8021#80综合查询系统,8050#80互联网服务平台,8060#80集成指挥平台</mrz></dataObj></result></body></root>"""

        # # 单表参数查询
        elif jkid == "81Q02":
            logger.info(u"获取单表策略")
            now = datetime.datetime.now()
            create_time = now.strftime("%Y-%m-%d %H:%M:%S")
            update_time = now.strftime("%Y-%m-%d %H:%M:%S")
            return """<?xml version="1.0" encoding="UTF-8"?><root><head><code>1</code><msg>null</msg></head><body><result><ywcode>1</ywcode><ywmsg>u"数据查询成功"</ywmsg><dataObj><bm>veh_check</bm><jgxtlb>10</jgxtlb><bmms>表05</bmms><clcjbj>1</clcjbj><sjczd>dlsj</sjczd><clqsrq>1991-01-01 20:00:00</clqsrq><clgltj>where xh>0</clgltj><clwcbj>0</clwcbj><zlkhdgllx>jdbc</zlkhdgllx><zlinsert>0</zlinsert><zlupdate>1</zlupdate><zldelete>0</zldelete><cjsj>{create_time}</cjsj><gxsj>{update_time}</gxsj></dataObj><dataObj><bm>drv_censor</bm><jgxtlb>10</jgxtlb><bmms>数据库表01</bmms><clcjbj>1</clcjbj><sjczd>syrq</sjczd><clqsrq>2000-12-05 00:00:00</clqsrq><clgltj>where id>=0</clgltj><clwcbj>0</clwcbj><zlkhdgllx>plsqldev</zlkhdgllx><zlinsert>1</zlinsert><zlupdate>1</zlupdate><zldelete>1</zldelete><cjsj>{create_time}</cjsj><gxsj>{update_time}</gxsj></dataObj><dataObj><bm>drv_exchange</bm><jgxtlb>10</jgxtlb><bmms>表02</bmms><clcjbj>1</clcjbj><sjczd>bhzrq</sjczd><clqsrq>1991-01-01 00:00:00</clqsrq><clgltj>where id>=0</clgltj><clwcbj>0</clwcbj><zlkhdgllx>jdbc</zlkhdgllx><zlinsert>1</zlinsert><zlupdate>0</zlupdate><zldelete>1</zldelete><cjsj>{create_time}</cjsj><gxsj>{update_time}</gxsj></dataObj><dataObj><bm>drv_health</bm><jgxtlb>10</jgxtlb><bmms>表03</bmms><clcjbj>1</clcjbj><sjczd>dlsj</sjczd><clqsrq>1991-04-10 20:00:00</clqsrq><clgltj>where id>=0</clgltj><clwcbj>0</clwcbj><zlkhdgllx>jdbc</zlkhdgllx><zlinsert>0</zlinsert><zlupdate>1</zlupdate><zldelete>0</zldelete><cjsj>{create_time}</cjsj><gxsj>{update_time}</gxsj></dataObj><dataObj><bm>drv_log</bm><jgxtlb>10</jgxtlb><bmms>表04</bmms><clcjbj>1</clcjbj><sjczd>clrq</sjczd><clqsrq>1991-01-01 20:00:00</clqsrq><clgltj>where id>=0</clgltj><clwcbj>0</clwcbj><zlkhdgllx>jdbc</zlkhdgllx><zlinsert>0</zlinsert><zlupdate>1</zlupdate><zldelete>0</zldelete><cjsj>{create_time}</cjsj><gxsj>{update_time}</gxsj></dataObj><dataObj><bm>veh_log</bm><jgxtlb>10</jgxtlb><bmms>表06</bmms><clcjbj>1</clcjbj><sjczd>dlsj</sjczd><clqsrq>1991-01-01 20:00:00</clqsrq><clgltj>where id>=0</clgltj><clwcbj>0</clwcbj><zlkhdgllx>jdbc</zlkhdgllx><zlinsert>0</zlinsert><zlupdate>1</zlupdate><zldelete>0</zldelete><cjsj>{create_time}</cjsj><gxsj>{update_time}</gxsj></dataObj></result></body></root>""".format(
                create_time=create_time, update_time=update_time)
        # 根据文件名查询存量数据日志解析文件最新的处理状态
        elif jkid == '81Q03':
            logger.info(u"获取存量文件状态")
            file_list = re.findall('<wjm>(.*?)</wjm>', UTF8XmlDoc)
            file_num = len(file_list)
            if not file_num:
                return """<?xml version="1.0" encoding="UTF-8" ?>
                                                <root><head><code>1</code><msg>u"数据查询成功"</msg></head>
                                                                <body><result><ywcode>0</ywcode><ywmsg>无数据</ywmsg></result></body></root>"""
            file_name_list = map(get_file_name, file_list)
            pre_file_list = os.listdir('/data/xml/pre')
            updated_file_list = os.listdir('/data/xml/uploaded')
            back_file_list = os.listdir('/data/xml/back')

            # pre_file_list = os.listdir('/data/test_api/rds_api/ttt/xml/pre')
            # updated_file_list = os.listdir('/data/test_api/rds_api/ttt/xml/updated')
            # back_file_list = os.listdir('/data/test_api/rds_api/ttt/xml/back')

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
                        logger.info("{file_name} 已入库".format(file_name=file_name))
                    else:
                        return_file_list.append({"file_status": 5, "file_name": file_name})
                        logger.info("{file_name} 要求重传".format(file_name=file_name))

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
        elif jkid == '81Q04':
            logger.info(u"获取增量文件状态")
            file_list = re.findall('<wjm>(.*?)</wjm>', UTF8XmlDocname)
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
                        logger.info("{file_name} 已入库".format(file_name=file_name))
                    else:
                        return_file_list.append({"file_status": 5, "file_name": file_name})
                        logger.info("{file_name} 要求重传".format(file_name=file_name))

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
        else:
            return "params error"

    @rpc(String, String, String, String, String, String, _returns=String)
    def writeRdsOut(self, xtlb='', jkxlh='', jkid='', babh='', wkmac='', UTF8XmlDoc=''):

        # 心跳状态上报
        if jkid == '81W01':
            logger.info(u"心跳状态上报")
            UTF8XmlDocname = """<?xml version="1.0" encoding="UTF-8"?>
                <root><WriteData>
                <babh>xxxxxxx</babh><sbrq>vfvfvfvf</sbrq>
                <cpusyl>1</cpusyl><ncsyl>1</ncsyl><cpsyl><20/cpsyl><xtfz>0.1</xtfz></WriteData></root>

                """

            return """<?xml version="1.0" encoding="UTF-8"?><root><head><code>1</code><msg>null</msg></head><body><wrongnum>0</wrongnum></body></root>"""
        # 采集软件运行状态写入
        elif jkid == '81W02':
            logger.info(u"采集软件运行状态写入")
            UTF8XmlDocname = """<?xml version="1.0" encoding="UTF-8"?>
                <root><WriteData>
                <babh>xxxxxxx</babh>
                <jgxtlb>21</jgxtlb>
                <fwqljzt>1</fwqljzt>
                <fwqcwms>1</fwqcwms>
                <sjkljzt>1</sjkljzt>
                <sjkcwms>1</sjkcwms>
                <zlhqfs>1</zlhqfs>
                <khdt>1</khdt>
                <khdcwms>1</khdcwms>
                <zxrzmlzt>1</zxrzmlzt>
                <zxrzcwms>1</zxrzcwms>
                <gdrzmlzt>1</gdrzmlzt>
                <gdrzcwms>1</gdrzcwms>
                <clyxzt>1</clyxzt>
                <zlyxzt>1</zlyxzt>          
                </WriteData></root>
                """
            return """<?xml version="1.0" encoding="UTF-8"?><root><head><code>1</code><msg>null</msg></head><body><wrongnum>0</wrongnum></body></root>"""
        # 存量数据处理状态写入
        elif jkid == '81W03':
            logger.info(u"存量数据处理状态写入")
            UTF8XmlDocname = """<?xml version="1.0" encoding="UTF-8"?>
                <root><WriteData>

                <jgxtlb>60</jgxtlb>
                <bm></bm>
                <cjzt></cjzt>
                <ccqdsj></ccqdsj>
                <zjqdsj></zjqdsj>
                <cjwcsj></cjwcsj>
                <sjzl></sjzl>
                <cjsjzl></cjsjzl>
                <cjwjs></cjwjs>
                <zhwjm></zhwjm>
                <rkzt></rkzt>
                <cwxxms></cwxxms>
                </WriteData></root>

                """
            return """<?xml version="1.0" encoding="UTF-8"?><root><head><code>1</code><msg>null</msg></head><body><wrongnum>0</wrongnum></body></root>"""
        # 存量数据断点写入
        elif jkid == '81W04':
            logger.info(u"存量数据断点写入")
            UTF8XmlDocname = """<?xml version="1.0" encoding="UTF-8"?>
                            <root><WriteData>
                            <bm>xx</bm>
                            <jgxtlb>60</jgxtlb>
                            <sjkbh>121</sjkbh>
                            <sjcq>2016-12-18 23:30:56</sjcq>
                            <sjcz>2016-12-23 23:30:56</sjcz>
                            <dqsjc>2016-12-25 23:30:56</dqsjc>
                            <wcbj>1</wcbj>
                            </WriteData></root>
                """

            return """<?xml version="1.0" encoding="UTF-8"?><root><head><code>1</code><msg>null</msg></head><body><wrongnum>0</wrongnum></body></root>"""
        # 存量数据文件信息写入
        elif jkid == '81W05':
            logger.info(u"存量数据文件信息写入")
            UTF8XmlDocname = """<?xml version="1.0" encoding="UTF-8"?>
                                                    <root><WriteData>
                                                    <jgxtlb>80</jgxtlb>
                                                    <bm>xx</bm>
                                                    <wjm></wjm>
                                                    <md5></md5>
                                                    <wjdx></wjdx>
                                                    <slj></slj>
                                                    <sjcq></sjcq>
                                                    <sjcz></sjcz>
                                                    <wjzt></wjzt>
                                                    <scsj></scsj>
                                                    <scfwqsj></scfwqsj>
                                                    <scbjsj></scbjsj>
                                                    <rksj></rksj>
                                                    <cwzt></cwzt>
                                                    <cwxxms></cwxxms>
                                                    <ccsj></ccsj>
                                                    </WriteData>
                                                    <WriteData>
                                                    </WriteData></root>
                """

            return """<?xml version="1.0" encoding="UTF-8"?><root><head><code>1</code><msg>null</msg></head><body><wrongnum>0</wrongnum></body></root>"""
        # 增量数据断点写入
        elif jkid == '81W06':
            logger.info(u"增量数据断点写入")
            UTF8XmlDocname = """<?xml version="1.0" encoding="UTF-8"?>
                                        <root><WriteData>
                                        <jgxtlb>21</jgxtlb>
                                        <scn>22</scn>
                                        <seq>221</seq>
                                        </WriteData></root>
                """

            return """<?xml version="1.0" encoding="UTF-8"?><root><head><code>1</code><msg>null</msg></head><body><wrongnum>0</wrongnum></body></root>"""
        # 增量数据文件信息写入
        elif jkid == '81W07':
            logger.info(u"增量数据文件信息写入")
            UTF8XmlDocname = """<?xml version="1.0" encoding="UTF-8"?>
                                                    <root><WriteData>
                                                    <jgxtlb>21</jgxtlb>
                                                    <wjm>14000022312322</wjm>
                                                    <md5>123rasdfaxc23rsd2ed</md5>
                                                    <wjdx>1539</wjdx>
                                                    <sjlinsert>931</sjlinsert>
                                                    <sjlupdate>23</sjlupdate>
                                                    <sjldelete>26</sjldelete>
                                                    <scnq>12345675</scnq>
                                                    <seqq>155</seqq>
                                                    <scnz>1233212</scnz>
                                                    <seqz>123</seqz>
                                                    <sywjm>1234565432234</sywjm>
                                                    <xywjm>123456765432</xywjm>
                                                    <wjzt>2</wjzt>
                                                    <scsj>2016-06-20 12:30:23</scsj>
                                                    <scfwqsj>2016-06-20 12:30:23</scfwqsj>
                                                    <cwzt>0</cwzt>
                                                    <cwxxms></cwxxms>
                                                    <ccsj>2016-06-20 12:30:23</ccsj>
                                                    </WriteData></root>
                """

            return """<?xml version="1.0" encoding="UTF-8"?><root><head><code>1</code><msg>null</msg></head><body><wrongnum>0</wrongnum></body></root>"""
        # DDL数据审计信息写入
        elif jkid == '81W08':
            logger.info(u"DDL数据审计信息写入")
            UTF8XmlDocname = """<?xml version="1.0" encoding="UTF-8"?>
                                    <root><WriteData>
                                    <jgxtlb>21</jgxtlb>
                                    <scn>123</scn>
                                    <seq>221</seq>
                                    <orauser>user</orauser>
                                    <oraschema>schema1</oraschema>
                                    <czlx>01</czlx>
                                    <dxlx>01</dxlx>
                                    <dxm>obj1</dxm>
                                    <czsj>2016-06-20 12:30:23</czsj>
                                    <nr>good</nr>
                                    </WriteData></root>
                """
            return """<?xml version="1.0" encoding="UTF-8"?><root><head><code>1</code><msg>null</msg></head><body><wrongnum>0</wrongnum></body></root>"""
        # 数据采集情况统计信息写入
        elif jkid == '81W09':
            logger.info(u"数据采集情况统计信息写入")
            UTF8XmlDocname = """<?xml version="1.0" encoding="UTF-8"?>

                                                <root><WriteData>
                                                <babh>ERTYUKJHGFGHJKUYGHJ</babh>
                                                <jgxtlb>21</jgxtlb>
                                                <tjrq>20171212</tjrq>
                                                <clcjl>20</clcjl>
                                                <cldcjl>20</cldcjl>
                                                <clwjs>20</clwjs>
                                                <clwjscs>20</clwjscs>
                                                <clwjdcs>20</clwjdcs>
                                                <zlcjl>20</zlcjl>
                                                <insert>20</insert>
                                                <update>20</update>
                                                <delete>20</delete>
                                                <zlwjs>20</zlwjs>
                                                <zlwjscs>20</zlwjscs>
                                                <zlwjdcs>20</zlwjdcs>
                                                <seqc>20</seqc>
                                                <ddll>20</ddll>
                                                </WriteData></root>
                """

            return """<?xml version="1.0" encoding="UTF-8"?><root><head><code>1</code><msg>null</msg></head><body><wrongnum>0</wrongnum></body></root>"""
        else:
            return "params error"


if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server

        server = make_server('0.0.0.0', 7792, Application([HelloWorldService], 'tns'))
        server.serve_forever()
        print 'listening on 127.0.0.1:7789'
        print 'wsdl is at: http://localhost:7789/SOAP/?wsdl'
    except ImportError:
        print "Error: example server code requires Python >= 2.5"
