# coding=utf-8
import re, time

from rest_framework import serializers
from collections import OrderedDict
from datetime import datetime, timedelta
from enum import Enum

from apps.driver.models import CodeInfo, DriverInfo, LoginTokenInfo, DriverAccountInfo
from apps.car.models import Carinfo
from utils import my_utils


class DriverEnum(Enum):
    """
    司机类型枚举类
    """
    # 性别类型
    MAN = 1  # 男
    WOMAN = 2  # 女


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
            login_token_expire_date = datetime.now() + timedelta(hours=2, minutes=0, seconds=0)
            token_info_list = LoginTokenInfo.objects.filter(DriverId=data['DriverId'])
            # 保存token
            if token_info_list:
                token_info_list.update(LoginToken=login_token, LoginTokenExpireDate=login_token_expire_date)
            else:
                LoginTokenInfo.objects.create(DriverId=data['DriverId'], CustomerId=0, LoginToken=login_token,
                                              LoginTokenExpireDate=login_token_expire_date)
        return data


class ExitLoginSerializer(serializers.ModelSerializer):
    tokenId = serializers.CharField(write_only=True, help_text='token', label='token',
                                    error_messages={'blank': 'token为必填项', 'required': "token为必填项",})
    LoginToken = serializers.CharField(read_only=True)
    LoginTokenExpireDate = serializers.DateTimeField(read_only=True)

    def validate_tokenId(self, tokenId):
        LoginTokenInfo.objects.filter(LoginToken=tokenId).first()
        if not LoginTokenInfo: raise serializers.ValidationError('token无效')
        tokenId_new =  my_utils.md5(tokenId + str(int(time.time())))[:32]
        return tokenId_new

    def validate(self, attrs):
        attrs['LoginToken'] = attrs['tokenId']
        attrs['LoginTokenExpireDate'] = datetime.now()
        return attrs

    class Meta:
        model = LoginTokenInfo
        fields = ['tokenId', 'LoginToken', 'LoginTokenExpireDate']


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
    """
    获取某个司机信息
    """

    class Meta:
        model = DriverInfo
        fields = '__all__'


class DriverBaseSerializer(serializers.ModelSerializer):
    DriverId = serializers.IntegerField(read_only=True, help_text='司机ID', label='司机ID')
    DriverName = serializers.CharField(read_only=True, help_text='司机名称', label='司机名称')
    CardId = serializers.CharField(read_only=True, min_length=15, max_length=18, help_text='身份证号码', label='身份证号码')
    CarId = serializers.IntegerField(read_only=True, help_text='车类型ID', label='车类型ID')
    CarNum = serializers.CharField(read_only=True, max_length=10, help_text='车牌号, 例：闽A 12345', label='车牌号')
    tokenId = serializers.CharField(read_only=True, help_text='token', label='token')
    ImageUrl = serializers.CharField(read_only=True, help_text='身份证正面', label='身份证正面')
    CardBackImageUrl = serializers.CharField(read_only=True, help_text='身份证背面', label='身份证背面')
    DriverLicenseUrl = serializers.CharField(read_only=True, help_text='驾驶证', label='驾驶证')
    LicenseImageUrl = serializers.CharField(read_only=True, help_text='行驶证', label='行驶证')

    Gender = serializers.IntegerField(read_only=True)
    DateOfBirth = serializers.DateField(read_only=True)
    Mobile = serializers.CharField(read_only=True)
    PassWord = serializers.CharField(read_only=True)
    NoTransitNum = serializers.IntegerField(read_only=True)
    InTransitNum = serializers.IntegerField(read_only=True)
    YesTransitNum = serializers.IntegerField(read_only=True)
    GoodsNum = serializers.IntegerField(read_only=True)
    CenterNum = serializers.IntegerField(read_only=True)
    NegativeNum = serializers.IntegerField(read_only=True)
    OrderTakeNum = serializers.IntegerField(read_only=True)
    IsCheck = serializers.IntegerField(read_only=True)
    HeadImageUrl = serializers.CharField(read_only=True)

    Status = serializers.IntegerField(read_only=True)
    AddUser = serializers.IntegerField(read_only=True)
    AddTime = serializers.DateTimeField(read_only=True)
    LastEditUser = serializers.IntegerField(read_only=True)
    LastEditTime = serializers.DateTimeField(read_only=True)

    @staticmethod
    def img_verify(url):
        try:
            f = open(url)
        except:
            return None
        return f

    class Meta:
        model = DriverInfo
        fields = '__all__'


class ApplyCheckDriverInfoSerializer(DriverBaseSerializer):
    """
    提交认证信息
    """
    DriverId = serializers.IntegerField(help_text='司机ID', label='司机ID',
                                        error_messages={"blank": "司机ID为必填", "required": "司机ID为必填"})
    DriverName = serializers.CharField(help_text='司机名称', label='司机名称',
                                       error_messages={"blank": "司机姓名为必填", "required": "司机姓名为必填"})
    CardId = serializers.CharField(min_length=15, max_length=18, help_text='身份证号码', label='身份证号码',
                                   error_messages={"blank": "身份证号码为必填", "required": "身份证号码为必填"})
    CarId = serializers.IntegerField(help_text='车类型ID', label='车类型ID',
                                     error_messages={"blank": "车类型ID为必填", "required": "车类型ID为必填"})
    CarNum = serializers.CharField(max_length=10, help_text='车牌号, 例：闽A 12345', label='车牌号',
                                   error_messages={"blank": "车牌号为必填", "required": "车牌号为必填"})
    tokenId = serializers.CharField(write_only=True, help_text='token', label='token',
                                    error_messages={"blank": "token为必填", "required": "token为必填"})
    ImageUrl = serializers.CharField(max_length=100, required=False, help_text='身份证正面', label='身份证正面')
    CardBackImageUrl = serializers.CharField(max_length=100, required=False, help_text='身份证背面', label='身份证背面')
    DriverLicenseUrl = serializers.CharField(max_length=100, required=False, help_text='驾驶证', label='驾驶证')
    LicenseImageUrl = serializers.CharField(max_length=100, required=False, help_text='行驶证', label='行驶证')

    def validate_CarId(self, CarId):
        car_info = Carinfo.objects.filter(CarId=CarId).first()
        if not car_info: raise serializers.ValidationError('车辆类型不合法')
        return CarId

    def validate_DriverId(self, DriverId):
        driver_info = DriverInfo.objects.filter(DriverId=DriverId).first()
        token_info = LoginTokenInfo.objects.filter(LoginToken=self.initial_data['tokenId']).first()
        if not driver_info: raise serializers.ValidationError('司机ID不合法')
        if not token_info or token_info.DriverId != driver_info.DriverId: raise serializers.ValidationError(
            '司机与token不匹配')
        return DriverId

    def validate_CardId(self, CardId):
        RE_ONE_CARDID = r'^[1-9]\d{5}\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}$'
        RE_TWO_CARDID = r'^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$'
        if not re.match(RE_ONE_CARDID, CardId) and not re.match(RE_TWO_CARDID, CardId):
            raise serializers.ValidationError('身份证不合法')
        return CardId

    def validate_CarNum(self, CarNum):
        RE_CARNUM = r'^[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领A-Z]{1}[A-Z]{1}\s*[A-Z0-9]{4}[A-Z0-9挂学警港澳]{1}$'
        if not re.match(RE_CARNUM, CarNum): raise serializers.ValidationError('车牌不合法')
        return CarNum

    def validate_ImageUrl(self, ImageUrl):
        if not DriverBaseSerializer.img_verify(ImageUrl): raise serializers.ValidationError("图片路径无效")
        return ImageUrl

    def validate_CardBackImageUrl(self, CardBackImageUrl):
        if not DriverBaseSerializer.img_verify(CardBackImageUrl): raise serializers.ValidationError("图片路径无效")
        return CardBackImageUrl

    def validate_DriverLicenseUrl(self, DriverLicenseUrl):
        if not DriverBaseSerializer.img_verify(DriverLicenseUrl): raise serializers.ValidationError("图片路径无效")
        return DriverLicenseUrl

    def validate_LicenseImageUrl(self, LicenseImageUrl):
        if not DriverBaseSerializer.img_verify(LicenseImageUrl): raise serializers.ValidationError("图片路径无效")
        return LicenseImageUrl

    def validate(self, attrs):
        # 删除tokenId
        del attrs['tokenId']
        # 时间
        attrs['LastEditTime'] = datetime.now()  # 最后修改时间
        # 审核结果
        attrs['IsCheck'] = 0
        return attrs

    class Meta:
        model = DriverBaseSerializer.Meta.model
        fields = ['DriverId', 'DriverName', 'CardId', 'CarNum', 'tokenId', 'ImageUrl', 'CardBackImageUrl', 'DriverLicenseUrl',
                  'LicenseImageUrl', 'LastEditTime', 'IsCheck']


class EditDriverInfoSerializer(DriverBaseSerializer):
    tokenId = serializers.CharField(write_only=True, help_text='token', label='token',
                                    error_messages={"blank": "token为必填", "required": "token为必填"})
    Gender = serializers.IntegerField(help_text='性别 1:男 2:女', label='性别',
                                      error_messages={"blank": "性别为必填", "required": "性别为必填"})
    DateOfBirth = serializers.DateField(help_text='生日 例：1990-01-01', label='生日',
                                      error_messages={"blank": "生日为必填", "required": "生日为必填"})
    HeadImageUrl = serializers.CharField(help_text='头像链接 例：media/driver/1/timg.jpg', label='头像链接',
                                      error_messages={"blank": "头像链接为必填", "required": "头像链接为必填"})

    def validate_Gender(self, Gender):
        if not Gender in [v.value for k, v in DriverEnum.__members__.items()]:
            raise serializers.ValidationError('性别参数错误')
        return Gender

    def validate_HeadImageUrl(self, HeadImageUrl):
        if not DriverBaseSerializer.img_verify(HeadImageUrl): raise serializers.ValidationError("图片路径无效")
        return HeadImageUrl

    def validate(self, attrs):
        # 时间
        attrs['LastEditTime'] = datetime.now()  # 最后修改时间

        return attrs

    class Meta:
        model = DriverBaseSerializer.Meta.model
        fields = ['tokenId', 'Gender', 'DateOfBirth', 'HeadImageUrl', 'LastEditTime']


class DriverImageUpLoadSerializer(serializers.Serializer):
    """
    司机图片上传
    """
    file = serializers.ImageField(help_text='图片', label='图片',
                                  error_messages={"blank": "图片为必填", "required": "图片为必填"})
    tokenId = serializers.CharField(help_text='token', label='token',
                                    error_messages={"blank": "token为必填", "required": "token为必填"})

    class Meta:
        fields = ['file']


class DriverAccountInfoSerializer(serializers.ModelSerializer):
    """
    获取司机账户
    """
    class Meta:
        model = DriverAccountInfo
        fields = '__all__'
