# coding:utf-8

from suds.client import Client
# hello_client = Client('http://40.125.204.79:7792/bigweb/services/SafeOutAccess?wsdl')
hello_client = Client('http://127.0.0.1:7792/bigweb/services/SafeOutAccess?wsdl')
print hello_client
hello_client.options.cache.clear()
# print hello_client
# result = hello_client.service.say_hello(
# """<?xml version="1.0" encoding="UTF-8" ?>
# <root>
#     <QueryCondition>
#             <wjm>11001901120180305000008</wjm>
#     </QueryCondition>
#     <QueryCondition>
#             <wjm>11001901120180305000010</wjm>
#     </QueryCondition>
#     <QueryCondition>
#             <wjm>09000109120171123000004</wjm>
#     </QueryCondition></root>""")
result = hello_client.service.queryRdsOut("80",
    jkxlb='',
    jkid='81Q01',
    babh='',
    wkmac='',
    UTF8XmlDoc='')

print result


result2 = hello_client.service.writeRdsOut("80",
    jkxlb='',
    jkid='81W01',
    babh='',
    wkmac='',
    UTF8XmlDoc='')
print result2