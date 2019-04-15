# coding=utf-8
from datetime import datetime, timedelta
from rest_framework import status
from rest_framework.response import Response

from apps.driver.models import LoginTokenInfo
from utils import my_reponse


def access_authority(func):
    def call_func(self, request, *args, **kwargs):
        token_id = request.query_params.get('tokenId')
        if not token_id:
            token_id = request.data.get('tokenId')

        if not token_id: return Response(my_reponse.get_response_error_dict(msg='没有权限'),
                                         status=status.HTTP_400_BAD_REQUEST)
        token_info = LoginTokenInfo.objects.filter(LoginToken=token_id).first()
        if not token_info: return Response(my_reponse.get_response_error_dict(msg='没有权限'),
                                           status=status.HTTP_400_BAD_REQUEST)

        token_info.LoginTokenExpireDate = datetime.now() + timedelta(hours=2, minutes=0, seconds=0)
        token_info.save()

        request.token_info = token_info
        self.token_info = token_info
        return func(self, request, *args, **kwargs)
    return call_func