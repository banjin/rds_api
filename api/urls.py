# coding:utf-8

from django.conf.urls import url
from views import FileStatus, face_back,SayHi

urlpatterns = [
    url(r'^file_back/$', FileStatus.as_view(), name='cc'),
    url(r'file/$', face_back),
    url(r'^hello/$', SayHi.as_view(), name='say')
]
