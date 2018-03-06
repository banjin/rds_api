# coding:utf-8

from django.conf.urls import url
from views import FileStatus, face_back

urlpatterns = [
    url(r'^file_back/$', FileStatus.as_view(), name='cc'),
    url(r'file/$', face_back),
]
