# coding:utf8

import json
import os
import commands
import re
import xml.etree.ElementTree as ET
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import FeedBackTestData
from .serializers import CommentSerializer
from django.http import JsonResponse as rsp, HttpResponse
import logging

logger = logging.getLogger('api')


def get_file_name(file_full_name):
    return os.path.splitext(file_full_name)[0]


class FileStatus(APIView):

    def post(self, request):
        """
        获取文件状态
        :param request:
        :return:
        """

        common_serializer = CommentSerializer(data=request.data)
        if not common_serializer.is_valid():
            return Response(common_serializer.errors)
        file_num = common_serializer.validated_data['wjs']
        file_names = common_serializer.validated_data['wjm']

        file_list = file_names.split(',')
        print file_list
        file_name_list = map(get_file_name, file_list)

        # 查找所有/data/xml/pre和/data/xml/updated/文件

        pre_file_list = os.listdir('/data/xml/pre')
        updated_file_list = os.listdir('/data/xml/uploaded')
        back_file_list = os.listdir('/data/xml/back')

        pre_file_name_ist = map(get_file_name,pre_file_list)
        update_file_name_list = map(get_file_name,updated_file_list)
        back_file_name_list = map(get_file_name,back_file_list)

        return_file_list = []

        # 根据文件名去文件夹下查找文件
        for file_name in file_name_list:
            if file_name not in back_file_name_list:
                if file_name in update_file_name_list:
                    return_file_list.append({"file_status": 4, "file_name": file_name + ".xml"})
                else:
                    return_file_list.append({"file_status": 5, "file_name": file_name + ".xml"})

        data = {
            "status": 0,
            "file_list": return_file_list,
            "file_num": file_num
        }

        # return JSONRenderer().render(data)
        return Response(data)


def face_back(request):
    """
    伪造安管平台接口，使用xml参数
    :param request:
    :return:
    """

    if request.method == 'POST':
        data = request.body
        file_list = re.findall('<wjm>(.*?)</wjm>', data)
        file_num = len(file_list)
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
                    return_file_list.append({"file_status": 4, "file_name": file_name + ".xml"})
                else:
                    return_file_list.append({"file_status": 5, "file_name": file_name + ".xml"})

        return_code = """<?xml version="1.0" encoding="UTF-8" ?>
                            <root>
                                    <fankui>
                                            <babh>120202000000000021</babh>
                                            <sqm>320202000000000023</sqm>
                                            <softip>192.168.19.101</softip>
                                            <softmac>OA-9D-3B-4C-5D-7A</softmac>
                                            <azdm>010031</azdm>
                                            <filelist wjs="{file_num}">
                                                {file_content}</filelist></fankui></root>"""

        a = ''
        for k, file_data in enumerate(return_file_list):
            a += """<file_info_{k}>
                        <wjm>{file_name}</wjm>
                        <type>{file_status}</type></file_info_{k}>""".format(k=k+1,
                                                                             file_name=file_data['file_name'],
                                                                             file_status=file_data['file_status'])

        data = return_code.format(file_num=file_num, file_content=a)
        return_data = {}
        return HttpResponse(data)
    else:
        return rsp({"status": 1, 'error': u'请使用post方法'})


class SayHi(APIView):
    """
    测试使用日志
    """
    def get(self, request, format=None):
        """
        获取hello
        :param request:
        :param format:
        :return:
        """
        logger.info("hi,mm")
        return Response({"status":0, "message": "hello, my love"})

