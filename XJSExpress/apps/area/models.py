from django.db import models

# Create your models here.
class Areainfo(models.Model):
    """
    区域
    """
    AreaId = models.IntegerField(db_column='AreaId', primary_key=True, verbose_name='id')  # Field name made lowercase.
    AreaName = models.CharField(db_column='AreaName', max_length=50, blank=True, null=True, verbose_name='区域名称')  # Field name made lowercase.
    Sort = models.IntegerField(db_column='Sort', blank=True, null=True, verbose_name='排序号')  # Field name made lowercase.
    ParentId = models.IntegerField(db_column='ParentId', blank=True, null=True, verbose_name='父id')  # Field name made lowercase.

    class Meta:
        db_table = 'c_areainfo'
        verbose_name = "区域"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.AreaName
