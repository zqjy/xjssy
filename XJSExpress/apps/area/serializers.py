# coding=utf-8
from rest_framework import serializers
from collections import OrderedDict

from apps.area.models import Areainfo
from utils import my_reponse


class AreainfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areainfo
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # data['children'] = []
        data['children'] = get_children(data['AreaId'], 'city')
        return data

class AreainfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areainfo
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['children'] = get_children(data['AreaId'], 'city')
        return data

def get_children(id, type):
    citys = Areainfo.objects.filter(ParentId=id)
    city_list = []
    for city in citys:
        city_Dict = OrderedDict()
        city_Dict['AreaId'] = city.AreaId
        city_Dict['AreaName'] = city.AreaName
        city_Dict['Sort'] = city.Sort
        city_Dict['ParentId'] = city.ParentId
        if type != 'district':
            city_Dict['children'] = get_children(city_Dict['AreaId'], 'district')
        else:
            city_Dict["children"] = []
            city_Dict["state"] = None
            city_Dict["ParentName"] = None

        city_list.append(city_Dict)
    return city_list






