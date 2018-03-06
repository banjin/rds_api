# coding:utf8

import json
import os
import commands

from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import FeedBackTestData
from .serializers import CommentSerializer


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
        updated_file_list = os.listdir('/data/xml/updated')
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



