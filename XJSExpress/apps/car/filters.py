from rest_framework import filters as drf_filter
from django_filters import rest_framework as filters
from django.db.models import Q

from apps.goods.models import GoodsInfo
from apps.car.models import Carinfo


class CarFilter(filters.FilterSet):
    CarType = filters.NumberFilter(method='car_type_filter', label='车辆类型', help_text='车辆类型 1：同城 2：全国')

    def car_type_filter(self, queryset, name, value):
        return queryset.filter(CarType=value)

    class Meta:
        model = Carinfo
        fields = '__all__'
