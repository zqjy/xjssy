import re, requests, json
from django.shortcuts import render
from rest_framework import mixins, viewsets, views
from rest_framework.response import Response
from rest_framework import status

from apps.area.models import Areainfo
from apps.area.serializers import AreainfoSerializer, AreainfoListSerializer
from utils import my_reponse


class AreaListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
    地区列表
    retrieve：
    获取单个地区信息
    retrieve_by_name:
    通过名称查找地区信息
    """
    queryset = Areainfo.objects.filter(ParentId=0)  # 获取省份
    # serializer_class = AreainfoSerializer  # 序列化同时补全数据

    # 重写list方法
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(my_reponse.get_response_dict(serializer.data))

    # 重写retrieve方法
    def retrieve(self, request, *args, **kwargs):
        print('*'*10)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(my_reponse.get_response_dict(serializer.data))

    def retrieve_by_name(self, request, area_name,*args, **kwargs):
        """
        通过名称获取地区信息
        :param request:
        :param area_name:
        :param args:
        :param kwargs:
        :return:
        """
        area_name = re.sub(r'[\s+|/]', '', area_name)
        instance = self.get_queryset().filter(AreaName=area_name).first()
        serializer = self.get_serializer(instance)
        return Response(my_reponse.get_response_dict(serializer.data))

    # 根据方法动态修改serializer类
    def get_serializer_class(self):
        if self.action=='retrieve':
            return AreainfoSerializer
        elif self.action=='list':
            return AreainfoListSerializer
        else:
            return AreainfoSerializer

    def get_queryset(self):
        if self.action=='retrieve_by_name':
            return Areainfo.objects.all()
        if self.action=='retrieve':
            return Areainfo.objects.all()
        else:
            return Areainfo.objects.filter(ParentId=0)



