import os, shutil
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from random import choice
from datetime import datetime

from apps.driver.models import CodeInfo, DriverInfo, LoginTokenInfo, DriverAccountInfo
from apps.driver.serializers import CodeInfoSerializer, FindPwdCodeInfoSerializer
from apps.driver.serializers import EditPasswordSerializer, DriverInfoSerializer, LoginSerializer, \
    DriverModelSerializer, ApplyCheckDriverInfoSerializer, DriverImageUpLoadSerializer, EditDriverInfoSerializer, \
    ExitLoginSerializer
from apps.driver.serializers import DriverAccountInfoSerializer
from apps.driver.filters import DriverFilter
from utils import my_reponse, my_utils, access_authority
from XJSExpress import settings


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
    retrieve:
    获取单个司机信息
    driver_image_upLoad:
    司机图片上传
    apply_check_driver_info：
    司机资料审核
    edit_driver_info:
    司机个人信息保存
    """
    queryset = DriverInfo.objects.all()

    # filter_backends = (DjangoFilterBackend,)  # 设置过滤
    # filter_class = DriverFilter

    def login_driver_info(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(my_reponse.get_response_dict(data=serializer.data, msg='登录成功'), status=status.HTTP_201_CREATED)

    @access_authority.access_authority
    def exit_login(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = LoginTokenInfo.objects.get(LoginTokenId=request.token_info.LoginTokenId)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(my_reponse.get_response_dict(data=serializer.data, msg='退出成功'), status=status.HTTP_201_CREATED)

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

    @access_authority.access_authority
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(my_reponse.get_response_dict(serializer.data), status=status.HTTP_200_OK)

    @access_authority.access_authority
    def apply_check_driver_info(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = DriverInfo.objects.get(DriverId=request.token_info.DriverId)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(my_reponse.get_response_dict(''), status=status.HTTP_201_CREATED)

    @access_authority.access_authority
    def driver_image_upLoad(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data_keys = serializer.validated_data.keys()
        if 'file' in data_keys:
            img_file = serializer.validated_data['file']
        else:
            img_file = None

        dirs = ''
        if img_file:
            dirs = settings.MEDIA_URL + 'driver/' + str(request.token_info.DriverId) + '/'
            save_path = dirs + img_file.name  # 文件保存路径
            try:
                if not os.path.exists(dirs):  # 检测订单文件夹路径
                    os.makedirs(dirs)
                with open(save_path, 'wb') as f:
                    for content in img_file.chunks():
                        f.write(content)
            except Exception as e:
                if os.path.exists(dirs):
                    shutil.rmtree(dirs)
                return Response(my_reponse.get_response_error_dict(msg='图片提交失败，请稍后再试'),
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(my_reponse.get_response_dict(dirs), status=status.HTTP_201_CREATED)

    @access_authority.access_authority
    def edit_driver_info(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = DriverInfo.objects.get(DriverId=request.token_info.DriverId)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(my_reponse.get_response_dict(''), status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.action == 'create':
            return DriverInfoSerializer
        elif self.action == 'update_driver':
            return EditPasswordSerializer
        elif self.action == 'login_driver_info':
            return LoginSerializer
        elif self.action == 'exit_login':
            return ExitLoginSerializer
        elif self.action == 'retrieve':
            return DriverModelSerializer
        elif self.action == 'apply_check_driver_info':
            return ApplyCheckDriverInfoSerializer
        elif self.action == 'driver_image_upLoad':
            return DriverImageUpLoadSerializer
        elif self.action == 'edit_driver_info':
            return EditDriverInfoSerializer
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


class DriverAccountInfoViewSet(viewsets.GenericViewSet):
    """
    retrieve:
    获取司机账户信息
    """
    queryset = DriverAccountInfo.objects.all()
    serializer_class = DriverAccountInfoSerializer

    @access_authority.access_authority
    def get_cash(self, request, *args, **kwargs):
        driver_account_info = DriverAccountInfo.objects.filter(DriverId=request.token_info.DriverId).first()
        if not driver_account_info:
            driver_account_info = DriverAccountInfo.objects.create(DriverId=request.token_info.DriverId,
                                                                   Balance=0.0, Arrival=0.0, NoArrival=0.0,
                                                                   AddTime=datetime.now(),
                                                                   LastEditTime=datetime.now())
        instance = driver_account_info
        serializer = self.get_serializer(instance)
        return Response(my_reponse.get_response_dict(serializer.data['Balance']), status=status.HTTP_200_OK)


