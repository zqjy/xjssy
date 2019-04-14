from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from random import choice
from datetime import datetime

from apps.driver.models import CodeInfo, DriverInfo, LoginTokenInfo
from apps.driver.serializers import CodeInfoSerializer, FindPwdCodeInfoSerializer
from apps.driver.serializers import EditPasswordSerializer, DriverInfoSerializer, LoginSerializer, DriverModelSerializer
from apps.driver.filters import DriverFilter
from utils import my_reponse, my_utils


class DriverInfoViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    create:
    保存司机信息
    update_driver
    修改司机信息
    login_driver_info:
    司机登录
    get_driver_model:
    获取司机信息
    """
    queryset = DriverInfo.objects.all()
    # filter_backends = (DjangoFilterBackend,)  # 设置过滤
    # filter_class = DriverFilter

    def login_driver_info(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(my_reponse.get_response_dict(data=serializer.data, msg='登录成功'), status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # ture 在验证失败的情况下自动返回400

        # 获取验证后的密码和电话
        password = serializer.validated_data["PassWord"]
        mobile = serializer.validated_data["mobile"]
        password = my_utils.md5(password)  # MD5加密

        driver_info = DriverInfo(Mobile=mobile, PassWord=password, AddTime=datetime.now(), LastEditTime=datetime.now())
        driver_info.save()
        return Response(my_reponse.get_response_dict(''), status=status.HTTP_201_CREATED)

    def update_driver(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # self.perform_update(serializer)
        # 获取验证后的密码和电话
        password = serializer.validated_data["PassWord"]
        mobile = serializer.validated_data["mobile"]
        password = my_utils.md5(password)  # MD5加密

        DriverInfo.objects.filter(Mobile=mobile).update(PassWord=password, LastEditTime=datetime.now())

        return Response(my_reponse.get_response_dict(''), status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        token_id = request.query_params.get('tokenId')
        if not token_id: return Response(my_reponse.get_response_error_dict(msg='没有权限'), status=status.HTTP_400_BAD_REQUEST)
        token_info = LoginTokenInfo.objects.filter(LoginToken=token_id).first()
        if not token_info: return Response(my_reponse.get_response_error_dict(msg='没有权限'), status=status.HTTP_400_BAD_REQUEST)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'create':
            return DriverInfoSerializer
        elif self.action == 'update_driver':
            return EditPasswordSerializer
        elif self.action == 'login_driver_info':
            return LoginSerializer
        elif self.action == 'retrieve':
            return DriverModelSerializer
        else:
            return DriverInfoSerializer




class CodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    create:
    保存验证码信息
    """

    def find_pwd_code_info(self, request):
        """
        发送修改密码验证码
        """
        return self.create(request)

    def create(self, request, *args, **kwargs):
        mobile = request.data.get("mobile")
        if not all([mobile]):
            mobile = request.data.get("mobile")
        request.data["mobile"] = mobile
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # ture 在验证失败的情况下自动返回400

        mobile = serializer.validated_data["mobile"]

        code = self.generate_code()

        # 缺少发送短信的逻辑

        code_record = CodeInfo.objects.filter(Mobile=mobile).first()
        if not code_record:
            code_record = CodeInfo(Mobile=mobile, CodeName=code, IsRead=0, AddTime=datetime.now())
            code_record.save()
        else:
            code_record.AddTime = datetime.now()
            code_record.CodeName = code
            code_record.save()

        return Response(my_reponse.get_response_dict(code), status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.action == 'create':
            return CodeInfoSerializer
        elif self.action == 'find_pwd_code_info':
            return FindPwdCodeInfoSerializer
        else:
            return CodeInfoSerializer

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(6):
            random_str.append(choice(seeds))  # 随机从字符串中取一个字符

        return "".join(random_str)
