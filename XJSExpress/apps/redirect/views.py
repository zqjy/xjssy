import re
import requests
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from rest_framework import mixins, viewsets, views, status
from rest_framework.response import Response
from django.http import JsonResponse

from utils import my_reponse, access_authority
from apps.redirect.serializers import RedirctSerializer
from apps.driver.models import LoginTokenInfo

# Create your views here.
class RedirectViewSet(viewsets.GenericViewSet):
    """
    get_area_info_model:
    获取单个区域接口
    get_area_info_list:
    获取区域接口
    get_car_info_list_json:
    有参获取车辆信息列表
    get_apply_car_list：
    无参获取车辆信息列表
    get_car_info_model_json:
    获取某个车辆信息
    get_order:
    获取司机个人订单
    """
    serializer_class = RedirctSerializer
    def get_area_info_list(self, request, *args, **kwargs):
        return redirect(reverse('area:list-list'))  # 重定向到area app list

    def get_area_info_model(self, request, *args, **kwargs):
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
        if not 'CarType' in  request.data.keys():
            return Response(my_reponse.get_response_error_dict(msg='缺少车类型参数'), status=status.HTTP_400_BAD_REQUEST)
        CarType = request.data['CarType']
        return redirect(reverse('car:list-list') + '?CarType=' + str(CarType))

    def get_apply_car_list(self, request, *args, **kwargs):
        return redirect(reverse('car:list-list'))

    def get_car_info_model_json(self, request, *args, **kwargs):
        car_id = request.data.get('carId')
        if not all([car_id]):
            car_id = request.data.get('CarId')

        # 验证参数合法性
        if not all([car_id]):
            # return redirect(reverse('car:list-list'))  # 重定向到car app list
            return Response(my_reponse.get_response_error_dict(), status=status.HTTP_400_BAD_REQUEST)
        if re.match(r'\d+', str(car_id)):
            return redirect(reverse('car:list-list') + str(car_id))  # 重定向到car app retrieve

    @access_authority.access_authority
    def get_driver_model(self, request, *args, **kwargs):
        token_id = request.data.get('tokenId')
        return redirect(reverse('driver:get_driver_model', kwargs={'pk': request.token_info.DriverId})  + '?tokenId=' + token_id)

    @access_authority.access_authority
    def get_order(self, request, *args, **kwargs):
        tokenId = request.data['tokenId']
        if not 'goodsStatus' in request.data.keys():
            return Response(my_reponse.get_response_error_dict(msg='缺少订单类型'), status=status.HTTP_400_BAD_REQUEST)
        goodsStatus = request.data['goodsStatus']

        redirect(reverse('goods:get_order') +
                 '?GoodsStatus=' + str(goodsStatus) +
                 '&tokenId=' + tokenId +
                 '&DriverId=' + str(request.token_info.DriverId))

    @access_authority.access_authority
    def get_cash(self, request, *args, **kwargs):
        redirect(reverse('driver:get_cash') + '?tokenId=' + request.data['tokenId'])



