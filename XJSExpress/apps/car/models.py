from django.db import models
from db_base.base_model import BaseModel


class Carinfo(BaseModel):
    CarId = models.AutoField(db_column='CarId', primary_key=True, verbose_name='车辆id')  # Field name made lowercase.
    CarName = models.CharField(db_column='CarName', max_length=50, blank=True, null=True, verbose_name='车辆名称')  # Field name made lowercase.
    Sort = models.IntegerField(db_column='Sort', blank=True, null=True, verbose_name='排序号')  # Field name made lowercase.
    ImageUrl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True, verbose_name='图片链接')  # Field name made lowercase.
    Load = models.CharField(db_column='Load', max_length=30, blank=True, null=True, verbose_name='重量')  # Field name made lowercase.
    LengthWidthHeight = models.CharField(db_column='LengthWidthHeight', max_length=30, blank=True, null=True, verbose_name='规格')  # Field name made lowercase.
    CargoVolume = models.CharField(db_column='CargoVolume', max_length=30, blank=True, null=True, verbose_name='货量')  # Field name made lowercase.
    Tips = models.CharField(db_column='Tips', max_length=255, blank=True, null=True, verbose_name='说明')  # Field name made lowercase.
    FixPrice = models.FloatField(db_column='FixPrice', blank=True, null=True, verbose_name='固定价格')  # Field name made lowercase.
    CarType = models.IntegerField(db_column='CarType', blank=True, null=True, verbose_name='车辆类型')  # Field name made lowercase.

    class Meta:
        db_table = 'm_carinfo'
        verbose_name = "车辆信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.CarName


class Carimageinfo(BaseModel):
    CarImageId = models.AutoField(db_column='CarImageId', primary_key=True, verbose_name='车辆图片id')  # Field name made lowercase.
    CarId = models.IntegerField(db_column='CarId', blank=True, null=True, verbose_name='车辆id')  # Field name made lowercase.
    ImageUrl = models.CharField(db_column='ImageUrl', max_length=100, blank=True, null=True, verbose_name='车辆图片链接')  # Field name made lowercase.
    IsCover = models.IntegerField(db_column='IsCover', blank=True, null=True, verbose_name='是否封面')  # Field name made lowercase.

    class Meta:
        db_table = 'm_carimageinfo'
        verbose_name = "车辆图片信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        car = Carinfo.objects.filter(CarId=self.CarId).first()
        if car:
            return car.CarName
        else:
            return self.ImageUrl
