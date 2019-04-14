import re
import requests
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from rest_framework import mixins, viewsets, views, status
from rest_framework.response import Response
from django.http import JsonResponse

from utils import my_reponse
from apps.redirect.serializers import RedirctSerializer
from apps.driver.models import LoginTokenInfo

# Create your views here.
class RedirectViewSet(viewsets.GenericViewSet):
    """
    get_area_info_json:
    获取区域接口
    get_car_info_list_json:
    获取车辆信息列表
    get_car_info_model_json:
    获取某个车辆信息
    """
    serializer_class = RedirctSerializer
    def get_area_info_list(self, request, *args, **kwargs):
        """
        获取区域接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return redirect(reverse('area:list-list'))  # 重定向到area app list

    def get_area_info_model(self, request, *args, **kwargs):
        """
        获取单个区域接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        area_name = request.data.get('AreaName')
        if not all([area_name]):
            area_name = request.data.get('areaName')

        # 验证参数合法性
        if not all([area_name]):
            return Response(my_reponse.get_response_error_dict(), status=400)  # 重定向到area app list
        if re.match(r'\w+', str(area_name)):
            return redirect(reverse('area:retrieve_by_name', kwargs=({'area_name': area_name})))  # 重定向到area app retrieve
        return Response(my_reponse.get_response_error_dict(), status=400)  # 重定向到area app list

    def get_car_info_list_json(self, request, *args, **kwargs):
        """
        获取车辆信息列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return redirect(reverse('car:list-list'))  # 重定向到car app list

    def get_car_info_model_json(self, request, *args, **kwargs):
        """
        获取某个车辆信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        car_id = request.data.get('carId')
        if not all([car_id]):
            car_id = request.data.get('CarId')

        # 验证参数合法性
        if not all([car_id]):
            # return redirect(reverse('car:list-list'))  # 重定向到car app list
            return Response(my_reponse.get_response_error_dict(), status=400)
        if re.match(r'\d+', str(car_id)):
            return redirect(reverse('car:list-list') + str(car_id))  # 重定向到car app retrieve

    def get_driver_model(self, request, *args, **kwargs):
        token_id = request.data.get('tokenId')
        if not token_id: return Response(my_reponse.get_response_error_dict(msg='没有权限'),
                                         status=status.HTTP_400_BAD_REQUEST)
        token_info = LoginTokenInfo.objects.filter(LoginToken=token_id).first()
        if not token_info: return Response(my_reponse.get_response_error_dict(msg='没有权限'),
                                           status=status.HTTP_400_BAD_REQUEST)
        return redirect(reverse('driver:get_driver_model', kwargs={'pk': token_info.DriverId})  + '?tokenId=' + token_id)






