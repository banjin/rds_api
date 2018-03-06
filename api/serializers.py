# coding:utf8
from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    wjs = serializers.IntegerField(required=True, help_text=u"文件数")
    wjm = serializers.CharField(required=True, max_length=2000, help_text=u"文件名")

    def validate_wjs(self, wjs):
        """
        Check that the type of the wjs.
        """
        if not isinstance(wjs, int):
            raise serializers.ValidationError("wjs post is not digit")
        return wjs
