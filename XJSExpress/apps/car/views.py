from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from apps.car.models import Carinfo, Carimageinfo
from apps.car.serializers import CarinfoListSerializer
from utils import my_reponse


class CarListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
    车辆列表
    retrieve：
    获取某个车信息
    """
    queryset = Carinfo.objects.all()  # 获取车辆
    serializer_class = CarinfoListSerializer

    # 重写
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(my_reponse.get_response_dict(serializer.data))

    # 重写
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(my_reponse.get_response_dict(serializer.data))


