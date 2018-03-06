# coding:utf-8

from django.conf.urls import url
from views import FileStatus

urlpatterns = [
    url(r'^file_back/$', FileStatus.as_view(), name='cc'),
]
