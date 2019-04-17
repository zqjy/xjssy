from enum import Enum
from rest_framework import serializers

class MyBaseSerializer(serializers.Serializer):
    Status = serializers.IntegerField(read_only=True, help_text='状态', label='状态')
    AddUser = serializers.IntegerField(read_only=True, help_text='添加人员', label='添加人员')
    AddTime = serializers.DateTimeField(read_only=True, help_text='添加时间', label='添加时间')
    LastEditUser = serializers.IntegerField(read_only=True, help_text='最后修改用户', label='最后修改用户')
    LastEditTime = serializers.DateTimeField(read_only=True, help_text='最后修改时间', label='最后修改时间')

    class Meta:
        abstract = True