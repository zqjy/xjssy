# coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# class Userinfo(models.Model):
#     """
#     用户
#     """
#     # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
#     userlogin = models.CharField(db_column='UserLogin', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     userpwd = models.CharField(db_column='UserPwd', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     roleid = models.IntegerField(db_column='RoleId', blank=True, null=True)  # Field name made lowercase.
#     username = models.CharField(db_column='UserName', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
#     adduser = models.IntegerField(db_column='AddUser', blank=True, null=True)  # Field name made lowercase.
#     addtime = models.DateTimeField(db_column='AddTime')  # Field name made lowercase.
#     lastedituser = models.IntegerField(db_column='LastEditUser', blank=True, null=True)  # Field name made lowercase.
#     lastedittime = models.DateTimeField(db_column='LastEditTime')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'userinfo'
#         verbose_name = "用户"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.username
#
class User(AbstractUser):
    """
    超级用户
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female",
                              verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")

    class Meta:
        db_table = 'user'
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username