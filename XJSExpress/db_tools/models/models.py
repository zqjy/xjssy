# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class CAreainfo(models.Model):
    areaid = models.IntegerField(db_column='AreaId', primary_key=True)  # Field name made lowercase.
    areaname = models.CharField(db_column='AreaName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_areainfo'


class CCodeinfo(models.Model):
    codeid = models.IntegerField(db_column='CodeId', primary_key=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    codename = models.CharField(db_column='CodeName', max_length=6, blank=True, null=True)  # Field name made lowercase.
    isread = models.IntegerField(db_column='IsRead', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_codeinfo'


class CCustomeraccountdetailsinfo(models.Model):
    customeraccountdetailsid = models.IntegerField(db_column='CustomerAccountDetailsId', primary_key=True)  # Field name made lowercase.
    customeraccountdetailstype = models.IntegerField(db_column='CustomerAccountDetailsType', blank=True, null=True)  # Field name made lowercase.
    customeraccountid = models.IntegerField(db_column='CustomerAccountId', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    accountmoney = models.FloatField(db_column='AccountMoney', blank=True, null=True)  # Field name made lowercase.
    ischeck = models.IntegerField(db_column='IsCheck', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.
    ordernum = models.CharField(db_column='OrderNum', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_customeraccountdetailsinfo'


class CCustomeraccountinfo(models.Model):
    customeraccountid = models.IntegerField(db_column='CustomerAccountId', primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    balance = models.FloatField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    arrival = models.FloatField(db_column='Arrival', blank=True, null=True)  # Field name made lowercase.
    noarrival = models.FloatField(db_column='NoArrival', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_customeraccountinfo'


class CCustomerinfo(models.Model):
    customerid = models.IntegerField(db_column='CustomerId', primary_key=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    weixinid = models.CharField(db_column='WeiXinId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    weixin = models.CharField(db_column='WeiXin', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PassWord', max_length=50, blank=True, null=True)  # Field name made lowercase.
    point = models.IntegerField(db_column='Point', blank=True, null=True)  # Field name made lowercase.
    publishnum = models.IntegerField(db_column='PublishNum', blank=True, null=True)  # Field name made lowercase.
    tradingnum = models.IntegerField(db_column='TradingNum', blank=True, null=True)  # Field name made lowercase.
    notransitnum = models.IntegerField(db_column='NoTransitNum', blank=True, null=True)  # Field name made lowercase.
    intransitnum = models.IntegerField(db_column='InTransitNum', blank=True, null=True)  # Field name made lowercase.
    yestransitnum = models.IntegerField(db_column='YesTransitNum', blank=True, null=True)  # Field name made lowercase.
    linkcustomerid = models.IntegerField(db_column='LinkCustomerId', blank=True, null=True)  # Field name made lowercase.
    ischeck = models.IntegerField(db_column='IsCheck', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_customerinfo'


class CDriveraccountdetailsinfo(models.Model):
    driveraccountdetailsid = models.IntegerField(db_column='DriverAccountDetailsId', primary_key=True)  # Field name made lowercase.
    driveraccountdetailstype = models.IntegerField(db_column='DriverAccountDetailsType', blank=True, null=True)  # Field name made lowercase.
    drivergoodsid = models.IntegerField(db_column='DriverGoodsId', blank=True, null=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsId', blank=True, null=True)  # Field name made lowercase.
    drivertype = models.CharField(db_column='DriverType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    driveraccountid = models.IntegerField(db_column='DriverAccountId', blank=True, null=True)  # Field name made lowercase.
    ordernum = models.CharField(db_column='OrderNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    driverid = models.IntegerField(db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accountmoney = models.FloatField(db_column='AccountMoney', blank=True, null=True)  # Field name made lowercase.
    accountcontent = models.CharField(db_column='AccountContent', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ischeck = models.IntegerField(db_column='IsCheck', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_driveraccountdetailsinfo'


class CDriveraccountinfo(models.Model):
    driveraccountid = models.IntegerField(db_column='DriverAccountId', primary_key=True)  # Field name made lowercase.
    driverid = models.IntegerField(db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
    balance = models.FloatField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    arrival = models.FloatField(db_column='Arrival', blank=True, null=True)  # Field name made lowercase.
    noarrival = models.FloatField(db_column='NoArrival', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_driveraccountinfo'


class CDrivergoodsinfo(models.Model):
    drivergoodsid = models.IntegerField(db_column='DriverGoodsId', primary_key=True)  # Field name made lowercase.
    driverid = models.IntegerField(db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsId', blank=True, null=True)  # Field name made lowercase.
    drivergoodstype = models.IntegerField(db_column='DriverGoodsType', blank=True, null=True)  # Field name made lowercase.
    isextract = models.IntegerField(db_column='IsExtract', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_drivergoodsinfo'


class CDriverinfo(models.Model):
    driverid = models.IntegerField(db_column='DriverId', primary_key=True)  # Field name made lowercase.
    drivername = models.CharField(db_column='DriverName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PassWord', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cardid = models.CharField(db_column='CardId', max_length=18, blank=True, null=True)  # Field name made lowercase.
    driverlicenseurl = models.CharField(db_column='DriverLicenseUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    licenseimageurl = models.CharField(db_column='LicenseImageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    notransitnum = models.IntegerField(db_column='NoTransitNum', blank=True, null=True)  # Field name made lowercase.
    intransitnum = models.IntegerField(db_column='InTransitNum', blank=True, null=True)  # Field name made lowercase.
    yestransitnum = models.IntegerField(db_column='YesTransitNum', blank=True, null=True)  # Field name made lowercase.
    goodsnum = models.IntegerField(db_column='GoodsNum', blank=True, null=True)  # Field name made lowercase.
    centernum = models.IntegerField(db_column='CenterNum', blank=True, null=True)  # Field name made lowercase.
    negativenum = models.IntegerField(db_column='NegativeNum', blank=True, null=True)  # Field name made lowercase.
    ordertakenum = models.IntegerField(db_column='OrderTakeNum', blank=True, null=True)  # Field name made lowercase.
    ischeck = models.IntegerField(db_column='IsCheck', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.
    carid = models.IntegerField(db_column='CarId', blank=True, null=True)  # Field name made lowercase.
    carnum = models.CharField(db_column='CarNum', max_length=10, blank=True, null=True)  # Field name made lowercase.
    headimageurl = models.CharField(db_column='HeadImageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cardbackimageurl = models.CharField(db_column='CardBackImageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_driverinfo'


class CDriverspeciallineinfo(models.Model):
    driverspeciallineid = models.IntegerField(db_column='DriverSpecialLineId', primary_key=True)  # Field name made lowercase.
    sendprovinceid = models.IntegerField(db_column='SendProvinceId', blank=True, null=True)  # Field name made lowercase.
    sendcityid = models.IntegerField(db_column='SendCityId', blank=True, null=True)  # Field name made lowercase.
    arriveprovinceid = models.IntegerField(db_column='ArriveProvinceId', blank=True, null=True)  # Field name made lowercase.
    arrivecityid = models.IntegerField(db_column='ArriveCityId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_driverspeciallineinfo'


class CFeedbackinfo(models.Model):
    feedbackid = models.IntegerField(db_column='FeedBackId', primary_key=True)  # Field name made lowercase.
    driverid = models.IntegerField(db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=20, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=200, blank=True, null=True)  # Field name made lowercase.
    feedbackdate = models.DateTimeField(db_column='FeedBackDate')  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    answerid = models.IntegerField(db_column='AnswerId', blank=True, null=True)  # Field name made lowercase.
    answercontent = models.CharField(db_column='AnswerContent', max_length=200, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_feedbackinfo'


class CGoodscommentimageinfo(models.Model):
    goodscommentimageid = models.IntegerField(db_column='GoodsCommentImageId', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsId', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ischeck = models.IntegerField(db_column='IsCheck', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_goodscommentimageinfo'


class CGoodsimageinfo(models.Model):
    goodsimageid = models.IntegerField(db_column='GoodsImageId', primary_key=True)  # Field name made lowercase.
    goodsid = models.IntegerField(db_column='GoodsId', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    iscover = models.IntegerField(db_column='IsCover', blank=True, null=True)  # Field name made lowercase.
    ischeck = models.IntegerField(db_column='IsCheck', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_goodsimageinfo'


class CGoodsinfo(models.Model):
    goodsid = models.IntegerField(db_column='GoodsId', primary_key=True)  # Field name made lowercase.
    goodsno = models.CharField(db_column='GoodsNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    outtradeno = models.CharField(db_column='OutTradeNo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    goodstype = models.IntegerField(db_column='GoodsType', blank=True, null=True)  # Field name made lowercase.
    goodsstatus = models.IntegerField(db_column='GoodsStatus', blank=True, null=True)  # Field name made lowercase.
    carid = models.IntegerField(db_column='CarId', blank=True, null=True)  # Field name made lowercase.
    carname = models.CharField(db_column='CarName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    modeofpayment = models.CharField(db_column='ModeOfPayment', max_length=20, blank=True, null=True)  # Field name made lowercase.
    goodsfreight = models.FloatField(db_column='GoodsFreight', blank=True, null=True)  # Field name made lowercase.
    customerpay = models.FloatField(db_column='CustomerPay', blank=True, null=True)  # Field name made lowercase.
    driverid = models.IntegerField(db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
    maketoorderdate = models.DateTimeField(db_column='MakeToOrderDate')  # Field name made lowercase.
    goodsname = models.CharField(db_column='GoodsName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    loadmodeid = models.IntegerField(db_column='LoadModeId', blank=True, null=True)  # Field name made lowercase.
    loadtime = models.DateTimeField(db_column='LoadTime')  # Field name made lowercase.
    sendprovinceid = models.IntegerField(db_column='SendProvinceId', blank=True, null=True)  # Field name made lowercase.
    sendcityid = models.IntegerField(db_column='SendCityId', blank=True, null=True)  # Field name made lowercase.
    senddistricid = models.IntegerField(db_column='SendDistricId', blank=True, null=True)  # Field name made lowercase.
    sendaddress = models.CharField(db_column='SendAddress', max_length=200, blank=True, null=True)  # Field name made lowercase.
    publishname = models.CharField(db_column='PublishName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    publishphone = models.CharField(db_column='PublishPhone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    publishdate = models.DateTimeField(db_column='PublishDate')  # Field name made lowercase.
    publishremark = models.CharField(db_column='PublishRemark', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arriveprovinceid = models.IntegerField(db_column='ArriveProvinceId', blank=True, null=True)  # Field name made lowercase.
    arrivecityid = models.IntegerField(db_column='ArriveCityId', blank=True, null=True)  # Field name made lowercase.
    arrivedistricid = models.IntegerField(db_column='ArriveDistricId', blank=True, null=True)  # Field name made lowercase.
    arriveaddress = models.CharField(db_column='ArriveAddress', max_length=200, blank=True, null=True)  # Field name made lowercase.
    unloadingtime = models.DateTimeField(db_column='UnloadingTime')  # Field name made lowercase.
    distance = models.FloatField(db_column='Distance', blank=True, null=True)  # Field name made lowercase.
    grabbing = models.DateTimeField(db_column='Grabbing')  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    km = models.FloatField(db_column='KM', blank=True, null=True)  # Field name made lowercase.
    ischeck = models.IntegerField(db_column='IsCheck', blank=True, null=True)  # Field name made lowercase.
    c_iscomment = models.IntegerField(db_column='C_IsComment', blank=True, null=True)  # Field name made lowercase.
    c_commentcontent = models.CharField(db_column='C_CommentContent', max_length=200, blank=True, null=True)  # Field name made lowercase.
    c_commentscore = models.IntegerField(db_column='C_CommentScore', blank=True, null=True)  # Field name made lowercase.
    d_iscomment = models.IntegerField(db_column='D_IsComment', blank=True, null=True)  # Field name made lowercase.
    d_commentcontent = models.CharField(db_column='D_CommentContent', max_length=200, blank=True, null=True)  # Field name made lowercase.
    d_commentscore = models.IntegerField(db_column='D_CommentScore', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.
    sendx = models.CharField(db_column='SendX', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sendy = models.CharField(db_column='SendY', max_length=30, blank=True, null=True)  # Field name made lowercase.
    arrivex = models.CharField(db_column='ArriveX', max_length=30, blank=True, null=True)  # Field name made lowercase.
    arrivey = models.CharField(db_column='ArriveY', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_goodsinfo'


class CLogintokeninfo(models.Model):
    logintokenid = models.IntegerField(db_column='LoginTokenId', primary_key=True)  # Field name made lowercase.
    driverid = models.IntegerField(db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    logintoken = models.CharField(db_column='LoginToken', max_length=32, blank=True, null=True)  # Field name made lowercase.
    logintokenexpiredate = models.DateTimeField(db_column='LoginTokenExpireDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_logintokeninfo'

class LoginTokenInfo(models.Model):
    LoginTokenId = models.IntegerField(db_column='LoginTokenId', primary_key=True, verbose_name='TokenID')  # Field name made lowercase.
    DriverId = models.IntegerField(db_column='DriverId', blank=True, null=True, verbose_name='司机ID')  # Field name made lowercase.
    CustomerId = models.IntegerField(db_column='CustomerId', blank=True, null=True, verbose_name='')  # Field name made lowercase.
    LoginToken = models.CharField(db_column='LoginToken', max_length=32, blank=True, null=True, verbose_name='')  # Field name made lowercase.
    LoginTokenExpireDate = models.DateTimeField(db_column='LoginTokenExpireDate', verbose_name='')  # Field name made lowercase.

    class Meta:
        db_table = 'c_logintokeninfo'
        verbose_name = "账户token信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.LoginTokenId


class Dictinfo(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    dictname = models.CharField(db_column='DictName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dicttype = models.IntegerField(db_column='DictType', blank=True, null=True)  # Field name made lowercase.
    dictvalue = models.IntegerField(db_column='DictValue', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dictinfo'


class MAnnouncementcenterinfo(models.Model):
    announcementcenterid = models.IntegerField(db_column='AnnouncementCenterId', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=200, blank=True, null=True)  # Field name made lowercase.
    carouseltime = models.DateField(db_column='CarouselTime', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_announcementcenterinfo'


class MAppversioninfo(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    appversion = models.CharField(db_column='AppVersion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    apptype = models.IntegerField(db_column='AppType', blank=True, null=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    appurl = models.CharField(db_column='AppUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_appversioninfo'


class MCarimageinfo(models.Model):
    carimageid = models.IntegerField(db_column='CarImageId', primary_key=True)  # Field name made lowercase.
    carid = models.IntegerField(db_column='CarId', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    iscover = models.IntegerField(db_column='IsCover', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_carimageinfo'


class MCarinfo(models.Model):
    carid = models.IntegerField(db_column='CarId', blank=True, null=True)  # Field name made lowercase.
    carname = models.CharField(db_column='CarName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    load = models.CharField(db_column='Load', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lengthwidthheight = models.CharField(db_column='LengthWidthHeight', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cargovolume = models.CharField(db_column='CargoVolume', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tips = models.CharField(db_column='Tips', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.
    fixprice = models.FloatField(db_column='FixPrice', blank=True, null=True)  # Field name made lowercase.
    cartype = models.IntegerField(db_column='CarType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_carinfo'


class MHelperinfo(models.Model):
    helperid = models.IntegerField(db_column='HelperId', primary_key=True)  # Field name made lowercase.
    helpername = models.CharField(db_column='HelperName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_helperinfo'


class MIntroduceinfo(models.Model):
    introduceid = models.IntegerField(db_column='IntroduceId', primary_key=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    point = models.IntegerField(db_column='Point', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_introduceinfo'


class MKmpriceinfo(models.Model):
    kmpriceid = models.IntegerField(db_column='KmPriceId', primary_key=True)  # Field name made lowercase.
    carid = models.IntegerField(db_column='CarId', blank=True, null=True)  # Field name made lowercase.
    kmpricetype = models.IntegerField(db_column='KmPriceType', blank=True, null=True)  # Field name made lowercase.
    startkm = models.FloatField(db_column='StartKm', blank=True, null=True)  # Field name made lowercase.
    startkmprice = models.FloatField(db_column='StartKmPrice', blank=True, null=True)  # Field name made lowercase.
    exceedstartkm = models.FloatField(db_column='ExceedStartKm', blank=True, null=True)  # Field name made lowercase.
    exceedstartkmprice = models.FloatField(db_column='ExceedStartKmPrice', blank=True, null=True)  # Field name made lowercase.
    startvolume = models.FloatField(db_column='StartVolume', blank=True, null=True)  # Field name made lowercase.
    startvolumeprice = models.FloatField(db_column='StartVolumePrice', blank=True, null=True)  # Field name made lowercase.
    exceedvolume = models.FloatField(db_column='ExceedVolume', blank=True, null=True)  # Field name made lowercase.
    exceedvolumeprice = models.FloatField(db_column='ExceedVolumePrice', blank=True, null=True)  # Field name made lowercase.
    startweight = models.FloatField(db_column='StartWeight', blank=True, null=True)  # Field name made lowercase.
    startweightprice = models.FloatField(db_column='StartWeightPrice', blank=True, null=True)  # Field name made lowercase.
    exceedstartweight = models.FloatField(db_column='ExceedStartWeight', blank=True, null=True)  # Field name made lowercase.
    exceedstartweightprice = models.FloatField(db_column='ExceedStartWeightPrice', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_kmpriceinfo'


class MLoginfo(models.Model):
    logid = models.IntegerField(db_column='LogId', primary_key=True)  # Field name made lowercase.
    logtype = models.IntegerField(db_column='LogType', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=200, blank=True, null=True)  # Field name made lowercase.
    logcontenr = models.TextField(db_column='LogContenr', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_loginfo'


class MNavigationbarinfo(models.Model):
    navigationbarid = models.IntegerField(db_column='NavigationBarId', primary_key=True)  # Field name made lowercase.
    navigationbartype = models.IntegerField(db_column='NavigationBarType', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_navigationbarinfo'


class MNewsinfo(models.Model):
    newsid = models.IntegerField(db_column='NewsId', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    newstypeid = models.IntegerField(db_column='NewsTypeId', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hit = models.IntegerField(db_column='Hit', blank=True, null=True)  # Field name made lowercase.
    istop = models.IntegerField(db_column='IsTop', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    publishdate = models.DateField(db_column='PublishDate', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_newsinfo'


class MNewstypeinfo(models.Model):
    newstypeid = models.IntegerField(db_column='NewsTypeId', primary_key=True)  # Field name made lowercase.
    newstypename = models.CharField(db_column='NewsTypeName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_newstypeinfo'


class MPointinfo(models.Model):
    pointid = models.IntegerField(db_column='PointId', primary_key=True)  # Field name made lowercase.
    pointtype = models.IntegerField(db_column='PointType', blank=True, null=True)  # Field name made lowercase.
    pointmoney = models.IntegerField(db_column='PointMoney', blank=True, null=True)  # Field name made lowercase.
    percentage = models.IntegerField(db_column='Percentage', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_pointinfo'


class MServicecenterinfo(models.Model):
    servicecenterid = models.IntegerField(db_column='ServiceCenterId', primary_key=True)  # Field name made lowercase.
    qq = models.CharField(db_column='QQ', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_servicecenterinfo'


class Pageurlinfo(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    urlname = models.CharField(db_column='UrlName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=100, blank=True, null=True)  # Field name made lowercase.
    icon = models.CharField(db_column='Icon', max_length=20, blank=True, null=True)  # Field name made lowercase.
    levelid = models.CharField(db_column='LevelID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pageurlinfo'


class Roleinfo(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roleinfo'


class Rolepageurlinfo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='RoleID', blank=True, null=True)  # Field name made lowercase.
    pageurlid = models.CharField(db_column='PageUrlID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rolepageurlinfo'

class Userinfo(models.Model):
    """
    用户
    """
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userlogin = models.CharField(db_column='UserLogin', max_length=20, blank=True, null=True)  # Field name made lowercase.
    userpwd = models.CharField(db_column='UserPwd', max_length=32, blank=True, null=True)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='RoleId', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
    lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
    lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userinfo'


