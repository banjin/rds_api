# coding:utf8
from rest_framework import serializers

from .models import Snippet


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


class SnippetSerializer(serializers.Serializer):
    pk=serializers.IntegerField(read_only=True)
    tittle = serializers.CharField(required=False,allow_blank=True)
    code = serializers.CharField()
    linenos = serializers.BooleanField(required=False)
    language = serializers.CharField(required=False)

    def create(self, validated_data):
        """
        :param validated_data:
        :return:
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tittle = validated_data.get('tittle', instance.tittle)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance


