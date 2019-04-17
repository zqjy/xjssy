# coding=utf-8
import re
from rest_framework import serializers
from collections import OrderedDict

from apps.car.models import Carinfo, Carimageinfo
from utils import my_reponse

class CarinfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carinfo
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if re.match(r'^/ImageUpload.*', data['ImageUrl']): data['ImageUrl'] =  '/media' + data['ImageUrl']
        data["CarImageIdList"] = None
        data["IsCover"] = None
        # data = my_reponse.get_response_dict(data)
        return data
