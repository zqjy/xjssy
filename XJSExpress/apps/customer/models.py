from django.db import models

from db_base.base_model import BaseModel


class CustomerInfo(BaseModel):
    CustomerId = models.AutoField(db_column='CustomerId', primary_key=True, help_text='顾客ID')
    CustomerName = models.CharField(db_column='CustomerName', max_length=20, blank=True, null=True, help_text='顾客名称')
    Gender = models.IntegerField(db_column='Gender', blank=True, null=True, help_text='性别')
    DateOfBirth = models.DateField(db_column='DateOfBirth', blank=True, null=True, help_text='生日')
    Mobile = models.CharField(db_column='Mobile', max_length=15, blank=True, null=True, help_text='电话')
    WeiXinId = models.CharField(db_column='WeiXinId', max_length=50, blank=True, null=True, help_text='微信号码')
    WeiXin = models.CharField(db_column='WeiXin', max_length=50, blank=True, null=True, help_text='微信名称')
    ImageUrl = models.CharField(db_column='ImageUrl', max_length=255, blank=True, null=True, help_text='头像链接')
    PassWord = models.CharField(db_column='PassWord', max_length=50, blank=True, null=True, help_text='密码')
    Point = models.IntegerField(db_column='Point', blank=True, null=True, help_text='积分')
    PublishNum = models.IntegerField(db_column='PublishNum', blank=True, null=True, help_text='发布数')
    TradingNum = models.IntegerField(db_column='TradingNum', blank=True, null=True, help_text='交易数')
    NoTransitNum = models.IntegerField(db_column='NoTransitNum', blank=True, null=True, help_text='未运输数')
    InTransitNum = models.IntegerField(db_column='InTransitNum', blank=True, null=True, help_text='运输中数')
    YesTransitNum = models.IntegerField(db_column='YesTransitNum', blank=True, null=True, help_text='已运达数')
    LinkCustomerId = models.IntegerField(db_column='LinkCustomerId', blank=True, null=True, help_text='推荐人ID')
    IsCheck = models.IntegerField(db_column='IsCheck', blank=True, null=True, help_text='审核状态')

    class Meta:
        db_table = 'c_customerinfo'
        verbose_name = "顾客信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.CustomerId)
    

class CustomerAccountDetailsInfo(BaseModel):
    CustomerAccountDetailsId = models.AutoField(db_column='CustomerAccountDetailsId', primary_key=True,  help_text='账户详细ID')
    CustomerAccountDetailsType = models.IntegerField(db_column='CustomerAccountDetailsType', blank=True, null=True, help_text='账户类型')
    CustomerAccountId = models.IntegerField(db_column='CustomerAccountId', blank=True, null=True, help_text='顾客账户ID')
    ImageUrl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True, help_text='')
    CustomerId = models.IntegerField(db_column='CustomerId', blank=True, null=True, help_text='账户信息ID')
    AccountMoney = models.FloatField(db_column='AccountMoney', blank=True, null=True, help_text='账户金额')
    IsCheck = models.IntegerField(db_column='IsCheck', blank=True, null=True, help_text='审核')
    OrderNum = models.CharField(db_column='OrderNum', max_length=50, blank=True, null=True, help_text='订单数量')

    class Meta:
        db_table = 'c_customeraccountdetailsinfo'
        verbose_name = "顾客账户详细信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.CustomerAccountDetailsId)


class CustomerAccountInfo(BaseModel):
    CustomerAccountId = models.AutoField(db_column='CustomerAccountId', primary_key=True, help_text='账户ID')
    CustomerId = models.IntegerField(db_column='CustomerId', blank=True, null=True, help_text='顾客ID')
    Balance = models.FloatField(db_column='Balance', blank=True, null=True, help_text='余额')
    Arrival = models.FloatField(db_column='Arrival', blank=True, null=True, help_text='到账')
    NoArrival = models.FloatField(db_column='NoArrival', blank=True, null=True, help_text='未到账')

    class Meta:
        db_table = 'c_customeraccountinfo'
        verbose_name = "顾客账户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.CustomerAccountId)