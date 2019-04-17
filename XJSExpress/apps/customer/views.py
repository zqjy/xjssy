import os, shutil
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from random import choice
from datetime import datetime

from apps.customer.models import CustomerInfo
from apps.customer.serializers import CustomerInfoSerializer, CustomerUpdateSerializer
from utils import my_reponse, my_utils, access_authority
from XJSExpress import settings


class CustomerInfoViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    retrieve:
    获取用户信息
    update:
    修改用户信息
    """
    queryset = CustomerInfo.objects.all()

    def retrieve(self, request, *args, **kwargs):
        resp = super().retrieve(request, *args, **kwargs)
        return Response(my_reponse.get_response_dict(resp.data), status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        print('*'*20)
        resp = super().update(request, *args, **kwargs)
        return Response(my_reponse.get_response_dict(resp.data), status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CustomerInfoSerializer
        elif self.action == 'update':
            return CustomerUpdateSerializer
        else:
            return CustomerInfoSerializer
