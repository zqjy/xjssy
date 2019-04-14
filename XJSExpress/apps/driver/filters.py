from rest_framework import filters as drf_filter
from django_filters import rest_framework as filters
from django.db.models import Q

from apps.driver.models import DriverInfo, LoginTokenInfo


class DriverFilter(filters.FilterSet):
    tokenId = filters.CharFilter(method='goods_type_filter', label='token', help_text='司机用户对应token')

    def goods_driver_filter(self, queryset, name, value):
        token_info = LoginTokenInfo.objects.filter(LoginToken=value).first()
        return queryset.filter(DriverId=token_info.DriverId).first()

    class Meta:
        model = DriverInfo
        fields = ['tokenId']
