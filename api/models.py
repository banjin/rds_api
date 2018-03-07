# coding:utf8
from django.db import models


class FeedBackTestData(models.Model):
    """ 模拟安管返回的入库重传文件名数据
    测试用,此数据库没有使用
    """
    file_name = models.CharField(u'文件名', max_length=128)
    # 反馈的文件状态 4 入库 5 重传
    type = models.SmallIntegerField(u'文件状态')

    class Meta:
        db_table = 'feedback_data'

    def __unicode__(self):
        return str(self.id)


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tittle = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(default='python', max_length=50)

    class Meta:
        ordering = ('created',)


