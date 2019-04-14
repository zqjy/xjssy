from rest_framework import filters as drf_filter
from django_filters import rest_framework as filters
from django.db.models import Q

from apps.goods.models import GoodsInfo
from apps.car.models import Carinfo


class GoodsFilter(filters.FilterSet):
    GoodsType = filters.NumberFilter(method='goods_type_filter', label='货单类型', help_text='货单类型 1：同城 2：全国')
    CarId = filters.NumberFilter(method='car_id_filter', label='订单车型', help_text='订单车型 接口地址：/H5Driver/GetCarInfoListJson')
    SendProvinceId = filters.NumberFilter(method='send_province_id_filter', label='起始地省份', help_text='起始地省份')
    SendCityId = filters.NumberFilter(method='send_city_id_filter', label='起始地城市', help_text='起始地城市')
    ArriveProvinceId = filters.NumberFilter(method='arrive_province_id_filter', label='目的地省份', help_text='目的地省份')
    ArriveCityId = filters.NumberFilter(method='arrive_city_id_filter', label='目的地城市', help_text='目的地城市')

    def goods_type_filter(self, queryset, name, value):
        return queryset.filter(GoodsType=value)

    def car_id_filter(self, queryset, name, value):
        car_info = Carinfo.objects.filter(CarId=value).first()
        if car_info:
            return queryset.filter(CarId=car_info.CarId)
        return queryset

    def send_province_id_filter(self, queryset, name, value):
        if value:
            return queryset.filter(SendProvinceId=value)
        return queryset

    def send_city_id_filter(self, queryset, name, value):
        if value:
            return queryset.filter(SendCityId=value)
        return queryset

    def arrive_province_id_filter(self, queryset, name, value):
        if value:
            return queryset.filter(ArriveProvinceId=value)
        return queryset

    def arrive_city_id_filter(self, queryset, name, value):
        if value:
            return queryset.filter(ArriveCityId=value)
        return queryset

    class Meta:
        model = GoodsInfo
        fields = ['GoodsType', 'CarId', 'SendProvinceId', 'SendCityId', 'ArriveProvinceId', 'ArriveCityId']
