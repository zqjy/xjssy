# coding=utf-8
import re, time

from rest_framework import serializers
from collections import OrderedDict
from datetime import datetime, timedelta

from apps.driver.models import CodeInfo, DriverInfo, LoginTokenInfo
from utils import my_utils


class BaseDriverSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11, help_text='电话号码', label='电话号码')
    PassWord = serializers.CharField(min_length=6, max_length=50, help_text='密码', label='密码',
                                     error_messages={
                                         "blank": "请输入密码",
                                         "required": "请输入密码",
                                         "max_length": "密码不大于50位",
                                         "min_length": "密码不小于6位"
                                     })

    def validate_mobile(self, mobile):
        pass

    def validate_PassWord(self, PassWord):
        pass

    class Meta:
        abstract = True


class LoginSerializer(BaseDriverSerializer):

    def validate_mobile(self, mobile):
        driver_list = DriverInfo.objects.filter(Mobile=self.initial_data["mobile"]).order_by("AddTime")
        if not driver_list:
            raise serializers.ValidationError("用户名或密码错误")
        return mobile

    def validate_PassWord(self, PassWord):
        PassWord = my_utils.md5(self.initial_data["PassWord"])
        driver_list = DriverInfo.objects.filter(Mobile=self.initial_data["mobile"], PassWord=PassWord).order_by(
            "AddTime")
        if not driver_list:
            raise serializers.ValidationError("用户名或密码错误")
        return PassWord

    def to_representation(self, instance):
        data = super().to_representation(instance)
        driver_info = DriverInfo.objects.filter(Mobile=data['mobile'], PassWord=data['PassWord'])
        # 生成Token
        raw_string = data['mobile'] + data['PassWord'] + str(int(time.time()))
        login_token = my_utils.md5(raw_string)[:32]
        if driver_info:
            del data['mobile']
            del data['PassWord']
            data['DriverId'] = driver_info[0].DriverId
            data['LoginToken'] = login_token
            # token过期时间
            login_token_expire_date = datetime.now() - timedelta(hours=2, minutes=0, seconds=0)
            token_info_list = LoginTokenInfo.objects.filter(DriverId=data['DriverId'])
            # 保存token
            if token_info_list:
                token_info_list.update(LoginToken=login_token, LoginTokenExpireDate=login_token_expire_date)
            else:
                LoginTokenInfo.objects.create(DriverId=data['DriverId'], CustomerId=0, LoginToken=login_token,
                                              LoginTokenExpireDate=login_token_expire_date)
        return data


class DriverInfoSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11, help_text='电话号码', label='电话号码')
    Code = serializers.CharField(min_length=6, max_length=6, help_text='验证码', label='验证码')
    PassWord = serializers.CharField(min_length=6, max_length=50, help_text='密码', label='密码',
                                     error_messages={
                                         "blank": "请输入密码",
                                         "required": "请输入密码",
                                         "max_length": "密码不大于50位",
                                         "min_length": "密码不小于6位"
                                     })

    def validate_Code(self, Code):
        """
        验证验证码
        :param Code:
        :return:
        """
        code_info = CodeInfo.objects.filter(Mobile=self.initial_data["mobile"]).order_by("-AddTime")
        if code_info:
            last_code = code_info[0]

            five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_mintes_ago > last_code.AddTime:
                raise serializers.ValidationError("验证码过期")

            if last_code.CodeName != Code:
                raise serializers.ValidationError("验证码错误")

        else:
            raise serializers.ValidationError("验证码错误")

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param mobile:
        :return:
        """
        # 手机是否注册
        if DriverInfo.objects.filter(Mobile=mobile).count():
            raise serializers.ValidationError("用户已存在")

        # 验证手机号码是否合法
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("电话号码非法")

        # 验证码发送频率
        one_mintes_ago = datetime.now() - timedelta(minutes=1)
        if CodeInfo.objects.filter(AddTime__gt=one_mintes_ago, Mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile


class EditPasswordSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11, help_text='电话号码', label='电话号码')
    Code = serializers.CharField(min_length=6, max_length=6, help_text='验证码', label='验证码')
    PassWord = serializers.CharField(min_length=6, max_length=50, help_text='密码', label='密码',
                                     error_messages={
                                         "blank": "请输入密码",
                                         "required": "请输入密码",
                                         "max_length": "密码不大于50位",
                                         "min_length": "密码不小于6位"
                                     })

    def validate_Code(self, Code):
        """
        验证验证码
        :param Code:
        :return:
        """
        code_info = CodeInfo.objects.filter(Mobile=self.initial_data["mobile"]).order_by("-AddTime")
        if code_info:
            last_code = code_info[0]

            five_mintes_ago = datetime.now() - timedelta(hours=2, minutes=5, seconds=0)
            if five_mintes_ago > last_code.AddTime:
                raise serializers.ValidationError("验证码过期")

            if last_code.CodeName != Code:
                raise serializers.ValidationError("验证码错误")

        else:
            raise serializers.ValidationError("验证码错误")

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param mobile:
        :return:
        """
        # 手机是否注册
        if not DriverInfo.objects.filter(Mobile=mobile).count():
            raise serializers.ValidationError("用户不存在")

        # 验证手机号码是否合法
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("电话号码非法")

        # 验证码发送频率
        one_mintes_ago = datetime.now() - timedelta(minutes=1)
        if CodeInfo.objects.filter(AddTime__gt=one_mintes_ago, Mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile


class CodeInfoSerializer(serializers.Serializer):
    """
    注册验证码
    """
    mobile = serializers.CharField(max_length=11, help_text='电话号码', label='电话号码')

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param mobile:
        :return:
        """
        # 手机是否注册
        if DriverInfo.objects.filter(Mobile=mobile).count():
            raise serializers.ValidationError("用户已存在")

        # 验证手机号码是否合法
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("电话号码非法")

        # 验证码发送频率
        one_mintes_ago = datetime.now() - timedelta(minutes=1)
        if CodeInfo.objects.filter(AddTime__gt=one_mintes_ago, Mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile


class FindPwdCodeInfoSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11, help_text='电话号码', label='电话号码')

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param mobile:
        :return:
        """
        # 手机是否注册
        if not DriverInfo.objects.filter(Mobile=mobile).count():
            raise serializers.ValidationError("用户不存在")

        # 验证手机号码是否合法
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("电话号码非法")

        # 验证码发送频率
        one_mintes_ago = datetime.now() - timedelta(minutes=0, seconds=1)
        if CodeInfo.objects.filter(AddTime__gt=one_mintes_ago, Mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile


class DriverModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = DriverInfo
        fields = '__all__'

