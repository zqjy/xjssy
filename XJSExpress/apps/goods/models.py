from django.db import models

from db_base.base_model import BaseModel


class GoodsInfo(BaseModel):
    GoodsId = models.AutoField(db_column='GoodsId', primary_key=True, verbose_name='货单ID')
    GoodsNo = models.CharField(db_column='GoodsNo', max_length=15, blank=True, null=True, verbose_name='货单号')
    OutTradeNo = models.CharField(db_column='OutTradeNo', max_length=32, blank=True, null=True, verbose_name='外部订单号')
    GoodsType = models.IntegerField(db_column='GoodsType', blank=True, null=True, verbose_name='货单类型', help_text='货单类型')
    GoodsStatus = models.IntegerField(db_column='GoodsStatus', blank=True, null=True, verbose_name='货单状态')
    CarId = models.IntegerField(db_column='CarId', blank=True, null=True, verbose_name='车辆ID')
    CarName = models.CharField(db_column='CarName', max_length=20, blank=True, null=True, verbose_name='车辆名称',
                               help_text='车辆类型中文名称')
    CustomerId = models.IntegerField(db_column='CustomerId', blank=True, null=True, verbose_name='顾客ID')
    ModeOfPayment = models.CharField(db_column='ModeOfPayment', max_length=20, blank=True, null=True,
                                     verbose_name='支付方式')
    GoodsFreight = models.FloatField(db_column='GoodsFreight', blank=True, null=True, verbose_name='运费')
    CustomerPay = models.FloatField(db_column='CustomerPay', blank=True, null=True, verbose_name='')
    DriverId = models.IntegerField(db_column='DriverId', blank=True, null=True, verbose_name='司机ID')
    MakeToOrderDate = models.DateTimeField(db_column='MakeToOrderDate', verbose_name='接单时间')
    GoodsName = models.CharField(db_column='GoodsName', max_length=30, blank=True, null=True, verbose_name='货物名称')
    LoadModeId = models.IntegerField(db_column='LoadModeId', blank=True, null=True, verbose_name='装车方式ID')
    LoadTime = models.DateTimeField(db_column='LoadTime', verbose_name='装车时间')
    SendProvinceId = models.IntegerField(db_column='SendProvinceId', blank=True, null=True, verbose_name='起始地省份ID',
                                         help_text='起始地省份ID')
    SendCityId = models.IntegerField(db_column='SendCityId', blank=True, null=True, verbose_name='起始地城市ID',
                                     help_text='起始地城市ID')
    SendDistricId = models.IntegerField(db_column='SendDistricId', blank=True, null=True, verbose_name='起始地区县ID',
                                        help_text='起始地区县ID')
    SendAddress = models.CharField(db_column='SendAddress', max_length=200, blank=True, null=True, verbose_name='起始地址')
    PublishName = models.CharField(db_column='PublishName', max_length=20, blank=True, null=True, verbose_name='发布姓名')
    PublishPhone = models.CharField(db_column='PublishPhone', max_length=15, blank=True, null=True, verbose_name='发布电话')
    PublishDate = models.DateTimeField(db_column='PublishDate', verbose_name='发布时间')
    PublishRemark = models.CharField(db_column='PublishRemark', max_length=50, blank=True, null=True, verbose_name='备注')
    ArriveProvinceId = models.IntegerField(db_column='ArriveProvinceId', blank=True, null=True, verbose_name='到达地省份ID',
                                           help_text='到达地省份ID')
    ArriveCityId = models.IntegerField(db_column='ArriveCityId', blank=True, null=True, verbose_name='到达地城市ID',
                                       help_text='到达地城市ID')
    ArriveDistricId = models.IntegerField(db_column='ArriveDistricId', blank=True, null=True, verbose_name='到达地区县ID',
                                          help_text='到达地区县ID')
    ArriveAddress = models.CharField(db_column='ArriveAddress', max_length=200, blank=True, null=True,
                                     verbose_name='到达地址')
    UnloadingTime = models.DateTimeField(db_column='UnloadingTime', verbose_name='卸货时间')
    Distance = models.FloatField(db_column='Distance', blank=True, null=True, verbose_name='距离')
    Grabbing = models.DateTimeField(db_column='Grabbing', verbose_name='抓取')
    Weight = models.FloatField(db_column='Weight', blank=True, null=True, verbose_name='重量')
    Volume = models.FloatField(db_column='Volume', blank=True, null=True, verbose_name='体积')
    KM = models.FloatField(db_column='KM', blank=True, null=True, verbose_name='距离')
    IsCheck = models.IntegerField(db_column='IsCheck', blank=True, null=True, verbose_name='是否入账')
    C_IsComment = models.IntegerField(db_column='C_IsComment', blank=True, null=True, verbose_name='客户是否允许评论')
    C_CommentContent = models.CharField(db_column='C_CommentContent', max_length=200, blank=True, null=True,
                                        verbose_name='客户评论内容')
    C_CommentScore = models.IntegerField(db_column='C_CommentScore', blank=True, null=True, verbose_name='客户评分')
    D_IsComment = models.IntegerField(db_column='D_IsComment', blank=True, null=True, verbose_name='司机是否允许评论')
    D_CommentContent = models.CharField(db_column='D_CommentContent', max_length=200, blank=True, null=True,
                                        verbose_name='司机评论内容')
    D_CommentScore = models.IntegerField(db_column='D_CommentScore', blank=True, null=True, verbose_name='司机评分')
    SendX = models.CharField(db_column='SendX', max_length=30, blank=True, null=True, verbose_name='起始地坐标X')
    SendY = models.CharField(db_column='SendY', max_length=30, blank=True, null=True, verbose_name='起始地坐标Y')
    ArriveX = models.CharField(db_column='ArriveX', max_length=30, blank=True, null=True, verbose_name='目标地坐标X')
    ArriveY = models.CharField(db_column='ArriveY', max_length=30, blank=True, null=True, verbose_name='目标地坐标Y')

    class Meta:
        db_table = 'c_goodsinfo'
        verbose_name = "货单信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.GoodsId)


class GoodsImageInfo(BaseModel):
    GoodsImageId = models.AutoField(db_column='GoodsImageId', primary_key=True, verbose_name='图片ID')
    GoodsId = models.IntegerField(db_column='GoodsId', blank=True, null=True, verbose_name='货单ID')
    ImageUrl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True, verbose_name='图片路径')
    IsCover = models.IntegerField(db_column='IsCover', blank=True, null=True, verbose_name='是否封面')
    IsCheck = models.IntegerField(db_column='IsCheck', blank=True, null=True, verbose_name='是否审核')

    class Meta:
        db_table = 'c_goodsimageinfo'
        verbose_name = "货单图片信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.GoodsImageId)


class GoodsCommentImageInfo(BaseModel):
    GoodsCommentImageId = models.AutoField(db_column='GoodsCommentImageId', primary_key=True, verbose_name='')
    Type = models.IntegerField(db_column='Type', blank=True, null=True, verbose_name='')
    GoodsId = models.IntegerField(db_column='GoodsId', blank=True, null=True, verbose_name='')
    ImageUrl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True, verbose_name='')
    IsCheck = models.IntegerField(db_column='IsCheck', blank=True, null=True, verbose_name='')

    class Meta:
        db_table = 'c_goodscommentimageinfo'
        verbose_name = "货单评论信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.GoodsCommentImageId)


class KmPriceInfo(BaseModel):
    KmPriceId = models.AutoField(db_column='KmPriceId', primary_key=True, verbose_name='主键ID', help_text='主键ID')
    CarId = models.IntegerField(db_column='CarId', blank=True, null=True, verbose_name='车辆类型ID', help_text='车辆类型ID')
    KmPriceType = models.IntegerField(db_column='KmPriceType', blank=True, null=True, verbose_name='计价方式',
                                      help_text='计价方式')
    StartKm = models.FloatField(db_column='StartKm', blank=True, null=True, verbose_name='起始公里数', help_text='起始公里数')
    StartKmPrice = models.FloatField(db_column='StartKmPrice', blank=True, null=True, verbose_name='起步价格',
                                     help_text='起步价格')
    ExceedStartKm = models.FloatField(db_column='ExceedStartKm', blank=True, null=True, verbose_name='超出公里数',
                                      help_text='超出公里数')
    ExceedStartKmPrice = models.FloatField(db_column='ExceedStartKmPrice', blank=True, null=True, verbose_name='超出价格',
                                           help_text='超出价格')
    StartVolume = models.FloatField(db_column='StartVolume', blank=True, null=True, verbose_name='起步体积',
                                    help_text='起步体积')
    StartVolumePrice = models.FloatField(db_column='StartVolumePrice', blank=True, null=True, verbose_name='起步体积价格',
                                         help_text='起步体积价格')
    ExceedVolume = models.FloatField(db_column='ExceedVolume', blank=True, null=True, verbose_name='超出体积',
                                     help_text='超出体积')
    ExceedVolumePrice = models.FloatField(db_column='ExceedVolumePrice', blank=True, null=True, verbose_name='超出体积价格',
                                          help_text='超出体积价格')
    StartWeight = models.FloatField(db_column='StartWeight', blank=True, null=True, verbose_name='起步重力',
                                    help_text='起步重力')
    StartWeightPrice = models.FloatField(db_column='StartWeightPrice', blank=True, null=True, verbose_name='起步重力价格',
                                         help_text='起步重力价格')
    ExceedStartWeight = models.FloatField(db_column='ExceedStartWeight', blank=True, null=True, verbose_name='超出体积',
                                          help_text='超出体积')
    ExceedStartWeightPrice = models.FloatField(db_column='ExceedStartWeightPrice', blank=True, null=True,
                                               verbose_name='超出体积价格', help_text='超出体积价格')

    class Meta:
        db_table = 'm_kmpriceinfo'
        verbose_name = "运费价格信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.KmPriceId)
