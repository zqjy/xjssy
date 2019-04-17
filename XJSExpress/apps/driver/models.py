from django.db import models

from db_base.base_model import BaseModel


class DriverInfo(BaseModel):
    DriverId = models.AutoField(db_column='DriverId', primary_key=True, verbose_name='司机ID')
    DriverName = models.CharField(db_column='DriverName', max_length=20, blank=True, null=True, verbose_name='司机名字')
    Gender = models.IntegerField(db_column='Gender', blank=True, null=True, verbose_name='性别')
    DateOfBirth = models.DateField(db_column='DateOfBirth', blank=True, null=True, verbose_name='生日')
    Mobile = models.CharField(db_column='Mobile', max_length=15, blank=True, null=True, verbose_name='手机')
    PassWord = models.CharField(db_column='PassWord', max_length=50, blank=True, null=True, verbose_name='密码')
    ImageUrl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True, verbose_name='身份证正面图片')
    CardId = models.CharField(db_column='CardId', max_length=18, blank=True, null=True, verbose_name='身份证号码')
    DriverLicenseUrl = models.CharField(db_column='DriverLicenseUrl', max_length=100, blank=True, null=True,
                                        verbose_name='驾驶证')
    LicenseImageUrl = models.CharField(db_column='LicenseImageUrl', max_length=100, blank=True, null=True,
                                       verbose_name='行驶证')
    NoTransitNum = models.IntegerField(db_column='NoTransitNum', blank=True, null=True, verbose_name='未运输数')
    InTransitNum = models.IntegerField(db_column='InTransitNum', blank=True, null=True, verbose_name='运输中数')
    YesTransitNum = models.IntegerField(db_column='YesTransitNum', blank=True, null=True, verbose_name='已运输数')
    GoodsNum = models.IntegerField(db_column='GoodsNum', blank=True, null=True, verbose_name='好评数')
    CenterNum = models.IntegerField(db_column='CenterNum', blank=True, null=True, verbose_name='中评数')
    NegativeNum = models.IntegerField(db_column='NegativeNum', blank=True, null=True, verbose_name='差评数')
    OrderTakeNum = models.IntegerField(db_column='OrderTakeNum', blank=True, null=True, verbose_name='接单次数')
    IsCheck = models.IntegerField(db_column='IsCheck', blank=True, null=True, verbose_name='审核结果')
    CarId = models.IntegerField(db_column='CarId', blank=True, null=True, verbose_name='车辆ID')
    CarNum = models.CharField(db_column='CarNum', max_length=10, blank=True, null=True, verbose_name='车牌')
    HeadImageUrl = models.CharField(db_column='HeadImageUrl', max_length=100, blank=True, null=True,
                                    verbose_name='头像图片')
    CardBackImageUrl = models.CharField(db_column='CardBackImageUrl', max_length=100, blank=True, null=True,
                                        verbose_name='身份证背面背面图片')

    class Meta:
        db_table = 'c_driverinfo'
        verbose_name = "司机信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.DriverName


class DriverAccountDetailsInfo(BaseModel):
    DriverAccountDetailsId = models.AutoField(db_column='DriverAccountDetailsId', primary_key=True,
                                                 verbose_name='账户详情ID')
    DriverAccountDetailsType = models.IntegerField(db_column='DriverAccountDetailsType', blank=True, null=True,
                                                   verbose_name='账户详情类型')
    DriverGoodsId = models.IntegerField(db_column='DriverGoodsId', blank=True, null=True, verbose_name='')
    GoodsId = models.IntegerField(db_column='GoodsId', blank=True, null=True, verbose_name='货物ID')
    DriverType = models.CharField(db_column='DriverType', max_length=20, blank=True, null=True, verbose_name='司机类型')
    DriverAccountId = models.IntegerField(db_column='DriverAccountId', blank=True, null=True, verbose_name='司机账户ID')
    OrderNum = models.CharField(db_column='OrderNum', max_length=50, blank=True, null=True, verbose_name='订单编号')
    DriverId = models.IntegerField(db_column='DriverId', blank=True, null=True, verbose_name='司机ID')
    ImageUrl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True, verbose_name='')
    AccountMoney = models.FloatField(db_column='AccountMoney', blank=True, null=True, verbose_name='账户金额')
    AccountContent = models.CharField(db_column='AccountContent', max_length=50, blank=True, null=True,
                                      verbose_name='账户内容')
    IsCheck = models.IntegerField(db_column='IsCheck', blank=True, null=True, verbose_name='是否结账')

    class Meta:
        db_table = 'c_driveraccountdetailsinfo'
        verbose_name = "司机账户详情信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.DriverAccountDetailsId


class DriverAccountInfo(BaseModel):
    DriverAccountId = models.AutoField(db_column='DriverAccountId', primary_key=True, verbose_name='司机账户ID')
    DriverId = models.IntegerField(db_column='DriverId', blank=True, null=True, verbose_name='司机ID')
    Balance = models.FloatField(db_column='Balance', blank=True, null=True, verbose_name='余额')
    Arrival = models.FloatField(db_column='Arrival', blank=True, null=True, verbose_name='到账')
    NoArrival = models.FloatField(db_column='NoArrival', blank=True, null=True, verbose_name='未到账')

    class Meta:
        db_table = 'c_driveraccountinfo'
        verbose_name = "司机账户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.DriverAccountId


class DriverGoodsInfo(BaseModel):
    DriverGoodsId = models.AutoField(db_column='DriverGoodsId', primary_key=True, verbose_name='司机货物ID')
    DriverId = models.IntegerField(db_column='DriverId', blank=True, null=True, verbose_name='司机ID')
    GoodsId = models.IntegerField(db_column='GoodsId', blank=True, null=True, verbose_name='货物ID')
    DriverGoodsType = models.IntegerField(db_column='DriverGoodsType', blank=True, null=True, verbose_name='司机货物类别')
    IsExtract = models.IntegerField(db_column='IsExtract', blank=True, null=True, verbose_name='是否提取')

    class Meta:
        db_table = 'c_drivergoodsinfo'
        verbose_name = "司机货物信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.DriverGoodsId


class DriverSpecialLineInfo(models.Model):
    DriverSpecialLineId = models.AutoField(db_column='DriverSpecialLineId', primary_key=True, verbose_name='司机专线ID')
    SendProvinceId = models.IntegerField(db_column='SendProvinceId', blank=True, null=True, verbose_name='')
    SendCityId = models.IntegerField(db_column='SendCityId', blank=True, null=True, verbose_name='')
    ArriveProvinceId = models.IntegerField(db_column='ArriveProvinceId', blank=True, null=True, verbose_name='')
    ArriveCityId = models.IntegerField(db_column='ArriveCityId', blank=True, null=True, verbose_name='')

    class Meta:
        db_table = 'c_driverspeciallineinfo'
        verbose_name = "司机专线信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.DriverSpecialLineId


class CodeInfo(models.Model):
    CodeId = models.AutoField(db_column='CodeId', primary_key=True, verbose_name='验证码ID')
    Mobile = models.CharField(db_column='Mobile', max_length=15, blank=True, null=True, verbose_name='电话号码')
    CodeName = models.CharField(db_column='CodeName', max_length=6, blank=True, null=True, verbose_name='验证码')
    IsRead = models.IntegerField(db_column='IsRead', blank=True, null=True, verbose_name='是否已读')
    AddTime = models.DateTimeField(db_column='AddTime', verbose_name='添加时间')

    class Meta:
        db_table = 'c_codeinfo'
        verbose_name = "验证码信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.CodeId


class LoginTokenInfo(models.Model):
    LoginTokenId = models.AutoField(db_column='LoginTokenId', primary_key=True, verbose_name='tokenID')
    DriverId = models.IntegerField(db_column='DriverId', blank=True, null=True, verbose_name='司机ID')
    CustomerId = models.IntegerField(db_column='CustomerId', blank=True, null=True, verbose_name='客户ID')
    LoginToken = models.CharField(db_column='LoginToken', max_length=32, blank=True, null=True, verbose_name='token信息')
    LoginTokenExpireDate = models.DateTimeField(db_column='LoginTokenExpireDate', verbose_name='过期时间')

    class Meta:
        db_table = 'c_logintokeninfo'
        verbose_name = "token信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.LoginTokenId
