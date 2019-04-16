from django.db import models
from enum import Enum


class BaseEnum(Enum):
    """
    基础枚举类
    """
    # 数据状态
    NORMAL = 0  # 正常
    DELETE = 1  # 删除
    GET_OUT = 2  # 违规
    CANCEL = 3  # 取消


class BaseModel(models.Model):
    """模型抽象基类"""
    Status = models.IntegerField(db_column='Status', blank=True, null=True, verbose_name='状态')
    AddUser = models.IntegerField(db_column='AddUser', blank=True, null=True, verbose_name='添加人员')
    AddTime = models.DateTimeField(db_column='AddTime', verbose_name='添加时间')
    LastEditUser = models.IntegerField(db_column='LastEditUser', blank=True, null=True, verbose_name='最后修改用户')
    LastEditTime = models.DateTimeField(db_column='LastEditTime', verbose_name='最后修改时间')

    class Meta:
        # 说明是一个抽象模型类
        abstract = True

