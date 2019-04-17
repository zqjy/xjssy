# coding=utf-8
import re, time

from rest_framework import serializers
from collections import OrderedDict
from datetime import datetime, timedelta
from enum import Enum

from apps.customer.models import CustomerInfo, CustomerAccountInfo, CustomerAccountDetailsInfo
from utils import my_utils
from db_base.base_serializers import MyBaseSerializer
from XJSExpress.settings import REGEX_MOBILE


class CustomerEnum(Enum):
    """
    司机类型枚举类
    """
    # 性别类型
    MAN = 1  # 男
    WOMAN = 2  # 女


class BaseCustomerSerializer(MyBaseSerializer):
    CustomerName = serializers.CharField(read_only=True, help_text='顾客名称', label='顾客名称')
    Gender = serializers.IntegerField(read_only=True, help_text='性别', label='性别')
    DateOfBirth = serializers.DateField(read_only=True, help_text='生日', label='生日')
    Mobile = serializers.CharField(read_only=True, help_text='电话', label='电话')
    WeiXinId = serializers.CharField(read_only=True, help_text='微信号码', label='微信号码')
    WeiXin = serializers.CharField(read_only=True, help_text='微信名称', label='微信名称')
    ImageUrl = serializers.CharField(read_only=True, help_text='头像链接', label='头像链接')
    PassWord = serializers.CharField(read_only=True, help_text='密码', label='密码')
    Point = serializers.IntegerField(read_only=True, help_text='积分', label='积分')
    PublishNum = serializers.IntegerField(read_only=True, help_text='发布数', label='发布数')
    TradingNum = serializers.IntegerField(read_only=True, help_text='交易数', label='交易数')
    NoTransitNum = serializers.IntegerField(read_only=True, help_text='未运输数', label='未运输数')
    InTransitNum = serializers.IntegerField(read_only=True, help_text='运输中数', label='运输中数')
    YesTransitNum = serializers.IntegerField(read_only=True, help_text='已运达数', label='已运达数')
    LinkCustomerId = serializers.IntegerField(read_only=True, help_text='推荐人ID', label='推荐人ID')
    IsCheck = serializers.IntegerField(read_only=True, help_text='审核状态', label='审核状态')

    class Meta:
        abstract = True


class CustomerInfoSerializer(serializers.ModelSerializer, BaseCustomerSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data['Point']: data['Point'] = 0
        if not data['NoTransitNum']: data['NoTransitNum'] = 0
        if not data['InTransitNum']: data['InTransitNum'] = 0
        if not data['YesTransitNum']: data['YesTransitNum'] = 0
        return data
    class Meta:
        model = CustomerInfo
        fields = '__all__'


class CustomerUpdateSerializer(serializers.ModelSerializer, BaseCustomerSerializer):
    DateOfBirth = serializers.DateField(required=False, help_text='生日', label='生日',
                                        error_messages={"blank": "生日为必填", "required": "生日为必填"})
    Mobile = serializers.CharField(required=False, help_text='电话', label='电话',
                                   error_messages={"blank": "电话为必填", "required": "电话为必填"})
    CustomerName = serializers.CharField(required=False, help_text='顾客名称', label='顾客名称',
                                         error_messages={"blank": "顾客名称为必填", "required": "顾客名称为必填"})
    Gender = serializers.IntegerField(required=False, help_text='性别', label='性别',
                                      error_messages={"blank": "性别为必填", "required": "性别为必填"})

    def validate_Mobile(self, Mobile):
        if not re.match(REGEX_MOBILE, Mobile):
            raise serializers.ValidationError("电话号码非法")
        return Mobile

    def validate_Gender(self, Gender):
        if not Gender in [v.value for k, v in CustomerEnum.__members__.items()]:
            raise serializers.ValidationError("性别异常")
        return Gender

    def validate(self, attrs):
        attrs['LastEditTime'] = datetime.now()
        return attrs

    class Meta:
        model = CustomerInfo
        fields = '__all__'

