import os, shutil, json, math
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.utils.serializer_helpers import ReturnList, ReturnDict
from random import choice
from datetime import datetime
from collections import OrderedDict
from django.db import transaction

from apps.goods.models import GoodsInfo, GoodsImageInfo, GoodsCommentImageInfo, KmPriceInfo
from apps.goods.serializers import GoodsInfoSerializer, CityWideSerializer, OnePieceSerializer, TheVehicleSerializer, \
    ReceiveSerializer, FinishSerializer, AdoptSerializer, GoodsEnum, DriverCommentSerializer, CommentImageSerializer, \
    CustomerCommentSerializer, CommentSerializer
from apps.goods.filters import GoodsFilter, CommentFilter
from apps.driver.models import DriverInfo, DriverAccountInfo, DriverGoodsInfo
from apps.customer.models import CustomerInfo
from apps.area.views import AreaListViewSet
from utils import my_reponse, my_utils, access_authority
from XJSExpress import settings


# 自定义分页类 代替REST_FRAMEWORK中分页配置
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_size_query_description = '每页返回条目数, 不传默认返回10条, 最大返回数50'
    page_query_param = 'page'
    page_query_description = '页码'
    max_page_size = 50

    def get_paginated_response(self, data):
        if isinstance(data, ReturnDict):
            list = []
            list.append(data)
            data = list

        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('Code', 1),
            ('Msg', '获取成功'),
            ('Success', True),
            ('results', []),
            ('Data', data)
        ]))


class GoodsInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    """
    list:
    获取所有货单数据
    retrieve:
    通过id获取订单详细信息
    city_wide_create:
    同城货单添加
    one_pice_create：
    全国零单添加
    the_vehicle_create：
    全国整单添加
    get_order:
    司机获取个人订单
    comment_list:
    获取评价信息
    """
    pagination_class = GoodsPagination  # 指定自定义分页类
    filter_backends = (DjangoFilterBackend,)  # 设置过滤
    filter_class = GoodsFilter

    # 设置了分页 list不返回结果
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(my_reponse.get_response_dict(serializer.data), status=status.HTTP_200_OK)

    def comment_list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(my_reponse.get_response_dict(serializer.data), status=status.HTTP_200_OK)

    @access_authority.access_authority
    def get_order(self, request, *args, **kwargs):
        if not 'DriverId' in request.query_params.keys():
            return Response(my_reponse.get_response_error_dict(msg='缺少司机Id'), status=status.HTTP_400_BAD_REQUEST)
        if not 'GoodsStatus' in request.query_params.keys():
            return Response(my_reponse.get_response_error_dict(msg='缺少订单类型'), status=status.HTTP_400_BAD_REQUEST)

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(my_reponse.get_response_dict(serializer.data), status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(my_reponse.get_response_dict(serializer.data), status=status.HTTP_200_OK)

    def city_wide_create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(my_reponse.get_response_dict(msg='保存成功'), status=status.HTTP_201_CREATED, headers=headers)

    def one_pice_create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def the_vehicle_create(self, request):
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # 获取图片文件
            data_keys = serializer.validated_data.keys()
            if 'GoodsImg' in data_keys:
                img_file = serializer.validated_data['GoodsImg']
                del serializer.validated_data['GoodsImg']
            else:
                img_file = None
            self.perform_create(serializer)
            data = serializer.data
            goods_no = data['GoodsNo']
            goods_info = GoodsInfo.objects.get(GoodsNo=goods_no)
            if img_file:
                dirs = settings.MEDIA_URL + 'goods/' + goods_no + '/'
                save_path = dirs + img_file.name  # 文件保存路径
                GoodsImageInfo.objects.create(GoodsId=goods_info.GoodsId, ImageUrl=save_path, IsCover=0,
                                              AddTime=datetime.now(), LastEditTime=datetime.now())
                try:
                    if not os.path.exists(dirs):  # 检测订单文件夹路径
                        os.makedirs(dirs)
                    with open(save_path, 'wb') as f:
                        for content in img_file.chunks():
                            f.write(content)
                except Exception as e:
                    if os.path.exists(dirs):
                        shutil.rmtree(dirs)
                    raise e

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @access_authority.access_authority
    @transaction.atomic
    def receive_goods(self, request, goods_id, *args, **kwargs):
        """
        接单
        """
        driver_info = DriverInfo.objects.filter(DriverId=request.token_info.DriverId).first()
        if driver_info.IsCheck != 3:
            return Response(my_reponse.get_response_error_dict(msg='请先提交资料，认证通过才能联系货主哦！')
                            , status=status.HTTP_400_BAD_REQUEST)
        goods_info = GoodsInfo.objects.filter(GoodsId=goods_id).first()
        if goods_info.MakeToOrderDate > goods_info.PublishDate:
            return Response(my_reponse.get_response_error_dict(msg='货单已被接，请选择其他货单'),
                            status=status.HTTP_400_BAD_REQUEST)
        if not goods_info:
            return Response(my_reponse.get_response_error_dict(msg='货单异常'), status=status.HTTP_400_BAD_REQUEST)
        partial = kwargs.pop('partial', False)
        instance = goods_info
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 创建司机订单数据
        driver_goods = DriverGoodsInfo.objects.filter(DriverId=driver_info.DriverI, GoodsId=goods_id).first()
        if not driver_goods:
            driver_goods = DriverGoodsInfo.objects.create(DriverId=driver_info.DriverId, GoodsId=goods_id,
                                                          DriverGoodsType=goods_info.GoodsType,
                                                          IsExtract=GoodsEnum.NO_EXTRACT,
                                                          AddTime=datetime.now(), LastEditTime=datetime.now())
        else:
            driver_goods.DriverGoodsType = goods_info.GoodsType
            driver_goods.IsExtract = GoodsEnum.NO_EXTRACT
            driver_goods.LastEditTime = datetime.now()
            driver_goods.save()

        return Response(my_reponse.get_response_dict('', msg='接单成功'), status=status.HTTP_201_CREATED)

    @access_authority.access_authority
    @transaction.atomic
    def adopt_goods(self, request, goods_id, *args, **kwargs):
        """
        司机确认取到货物
        """
        driver_info = DriverInfo.objects.filter(DriverId=request.token_info.DriverId).first()
        goods_info = GoodsInfo.objects.filter(GoodsId=goods_id).first()
        if goods_info.MakeToOrderDate < goods_info.PublishDate:
            return Response(my_reponse.get_response_error_dict(msg='货单没有被接，不能完成'), status=status.HTTP_400_BAD_REQUEST)
        if not goods_info:
            return Response(my_reponse.get_response_error_dict(msg='货单异常'), status=status.HTTP_400_BAD_REQUEST)

        partial = kwargs.pop('partial', False)
        instance = goods_info
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 修改司机货单表
        driver_goods = DriverGoodsInfo.objects.filter(DriverId=driver_info.DriverI, GoodsId=goods_id).first()
        if not driver_goods:
            transaction.rollback()
            return Response(my_reponse.get_response_error_dict(msg='司机货单数据异常'), status=status.HTTP_400_BAD_REQUEST)
        driver_goods.IsExtract = GoodsEnum.YES_EXTRACT
        driver_goods.LastEditTime = datetime.now()
        driver_goods.save()
        return Response(my_reponse.get_response_dict('', msg='获取确认接收'), status=status.HTTP_201_CREATED)

    @transaction.atomic
    def finish_goods(self, request, goods_id, *args, **kwargs):
        """
        完成订单
        """
        goods_info = GoodsInfo.objects.filter(GoodsId=goods_id).first()
        if goods_info.MakeToOrderDate < goods_info.PublishDate:
            return Response(my_reponse.get_response_error_dict(msg='货单没有被接，不能完成'), status=status.HTTP_400_BAD_REQUEST)
        if not goods_info:
            return Response(my_reponse.get_response_error_dict(msg='货单异常'), status=status.HTTP_400_BAD_REQUEST)
        partial = kwargs.pop('partial', False)
        instance = goods_info
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 更新顾客数据
        customer_id = goods_info.CustomerId
        customer_info = CustomerInfo.objects.filter(CustomerId=customer_id).first()
        if not customer_info:
            transaction.rollback()
            return Response(my_reponse.get_response_error_dict(msg='货单没有对应的顾客'), status=status.HTTP_400_BAD_REQUEST)
        # 交易数
        customer_info.TradingNum = customer_info.TradingNum if customer_info.TradingNum else 0
        customer_info.TradingNum += 1
        # 运输中数
        customer_info.InTransitNum = customer_info.InTransitNum if customer_info.InTransitNum else 1
        customer_info.InTransitNum -= 1
        # 运达数
        customer_info.YesTransitNum = customer_info.YesTransitNum if customer_info.YesTransitNum else 0
        customer_info.YesTransitNum += 1
        # 积分
        customer_info.Point = customer_info.Point if customer_info.Point else 0
        price = goods_info.GoodsFreight
        customer_info.Point += price / 10
        # 保存
        customer_info.save()

        # 更新司机数据
        driver_id = goods_info.DriverId
        driver_info = DriverInfo.objects.filter(DriverId=driver_id).first()
        if not driver_info:
            transaction.rollback()
            return Response(my_reponse.get_response_error_dict(msg='货单没有对应的司机'), status=status.HTTP_400_BAD_REQUEST)
        # 运输中数
        driver_info.InTransitNum = customer_info.InTransitNum if customer_info.InTransitNum else 1
        driver_info.InTransitNum -= 1
        # 运达数
        driver_info.YesTransitNum = customer_info.YesTransitNum if customer_info.YesTransitNum else 0
        driver_info.YesTransitNum += 1
        # 接单次数
        driver_info.OrderTakeNum = driver_info.OrderTakeNum if driver_info.OrderTakeNum else 0
        driver_info.OrderTakeNum += 1
        # 保存
        driver_info.save()
        # 更新司机账户信息
        driver_account = DriverAccountInfo.objects.filter(DriverId=driver_id).first()
        if not driver_account:
            driver_account = DriverAccountInfo.objects.create(DriverId=driver_id, Balance=0.0, Arrival=0.0,
                                                              NoArrival=0.0,
                                                              LastEditTime=datetime.now(), AddTime=datetime.now())
        driver_account.Balance = goods_info.GoodsFreight
        driver_account.save()

        return Response(my_reponse.get_response_dict('', msg='货单完成'), status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.action == 'city_wide_create':
            return CityWideSerializer
        elif self.action == 'one_pice_create':
            return OnePieceSerializer
        elif self.action == 'the_vehicle_create':
            return TheVehicleSerializer
        elif self.action == 'receive_goods':
            return ReceiveSerializer
        elif self.action == 'finish_goods':
            return FinishSerializer
        elif self.action == 'adopt_goods':
            return AdoptSerializer
        elif self.action == 'comment_list':
            return CommentSerializer
        else:
            return GoodsInfoSerializer

    def get_queryset(self):
        if self.action == 'get_order':
            return GoodsInfo.objects.all().order_by('-PublishDate')
        elif self.action == 'receive_goods':
            return GoodsInfo.objects.all().order_by('-PublishDate')
        else:
            # GoodsStatus 1：未运输 2：运输中 3：已到达
            # return GoodsInfo.objects.filter(GoodsStatus=1).order_by('-PublishDate')
            return GoodsInfo.objects.all().order_by('-PublishDate')


class PriceInfoViewSet(viewsets.GenericViewSet):
    def get_price(self, request, car_id, type, sp_id, sc_id, s_addr, dp_id, dc_id, d_addr, weight=0.0, volume=0.0):
        """
        获取订单价格
        :param request:
        :param car_id: 车辆类型ID
        :param sp_id: 起始地省份ID
        :param sc_id: 起始地市ID
        :param s_addr: 起始地详细地址
        :param dp_id: 目的地省份ID
        :param dc_id: 目的地市ID
        :param d_addr: 目的地详细地址
        :param weight: 重量 全国零单使用
        :param volume: 体积 全国零单使用
        :return: 订单价格
        """
        return my_utils.get_price_static(car_id, type, sp_id, sc_id, s_addr, dp_id, dc_id, d_addr, weight, volume)


class CommentViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    comment_img_upload：
    评论图片保存

    """
    filter_backends = (DjangoFilterBackend,)  # 设置过滤
    filter_class = CommentFilter
    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        return Response(my_reponse.get_response_dict(res.data), status=status.HTTP_200_OK)

    def comment_img_upload(self, request):
        serializer = self.get_serializer(data=request.data)
        ret = serializer.is_valid(raise_exception=False)
        if not ret: return Response(my_reponse.get_response_error_dict(data=serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        Type = serializer.validated_data["Type"]
        GoodsId = serializer.validated_data["GoodsId"]
        goods_info = GoodsInfo.objects.get(GoodsId=GoodsId)
        save_path = my_utils.upload_img(serializer, 'ImageUrl', 'goods/' + goods_info.GoodsNo + '/')
        if save_path is None:
            save_path = ''
        elif isinstance(save_path, str):
            pass
        else:
            return Response(my_reponse.get_response_error_dict(data=save_path.data), status=status.HTTP_504_GATEWAY_TIMEOUT)

        GoodsCommentImageInfo.objects.create(Type=Type, GoodsId=GoodsId, ImageUrl=save_path,
                                             AddTime=datetime.now(), LastEditTime=datetime.now())
        serializer.data['ImageUrl'] = save_path
        return Response(my_reponse.get_response_dict(serializer.data), status=status.HTTP_201_CREATED)

    @access_authority.access_authority
    @transaction.atomic
    def driver_comment_goods(self, request, goods_id, *args, **kwargs):
        """
        货单评价
        """
        goods_info = GoodsInfo.objects.filter(GoodsId=goods_id).first()
        if goods_info.GoodsStatus != GoodsEnum.YES_TRANSPORT.value:
            return Response(my_reponse.get_response_error_dict(msg='当前货单不能评价'), status=status.HTTP_400_BAD_REQUEST)
        if not goods_info:
            return Response(my_reponse.get_response_error_dict(msg='货单异常'), status=status.HTTP_400_BAD_REQUEST)

        if request.token_info.DriverId and request.token_info.DriverId == goods_info.DriverId:
            partial = kwargs.pop('partial', False)
            instance = goods_info
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            ret = serializer.is_valid(raise_exception=False)
            if not ret: return Response(my_reponse.get_response_error_dict(msg='error', data=serializer.errors),
                                        status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(my_reponse.get_response_dict(), status=status.HTTP_201_CREATED)
        else:
            return Response(my_reponse.get_response_error_dict(msg='token异常或订单与司机不匹配'), status=status.HTTP_400_BAD_REQUEST)

    @access_authority.access_authority
    @transaction.atomic
    def customer_comment_goods(self, request, goods_id, *args, **kwargs):
        """
        货单评价
        """
        goods_info = GoodsInfo.objects.filter(GoodsId=goods_id).first()
        if goods_info.GoodsStatus != GoodsEnum.YES_TRANSPORT.value:
            return Response(my_reponse.get_response_error_dict(msg='当前货单不能评价'), status=status.HTTP_400_BAD_REQUEST)
        if not goods_info:
            return Response(my_reponse.get_response_error_dict(msg='货单异常'), status=status.HTTP_400_BAD_REQUEST)

        if request.token_info.CustomerId and request.token_info.CustomerId == goods_info.CustomerId:
            partial = kwargs.pop('partial', False)
            instance = goods_info
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            ret = serializer.is_valid(raise_exception=False)
            if not ret: return Response(my_reponse.get_response_error_dict(msg='error', data=serializer.errors),
                                        status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(my_reponse.get_response_dict(), status=status.HTTP_201_CREATED)
        else:
            return Response(my_reponse.get_response_error_dict(msg='token异常或订单与顾客不匹配'), status=status.HTTP_400_BAD_REQUEST)


    def get_serializer_class(self):
        if self.action == 'comment_img_upload':
            return CommentImageSerializer
        elif self.action == 'driver_comment_goods':
            return DriverCommentSerializer
        elif self.action == 'customer_comment_goods':
            return CustomerCommentSerializer
        else:
            return CommentImageSerializer

    def get_queryset(self):
        if self.action == 'comment_img_upload':
            return GoodsCommentImageInfo.objects.all()
        elif self.action == 'driver_comment_goods' \
                or self.action == 'customer_comment_goods':
            return GoodsInfo.objects.all()
        else:
            return GoodsCommentImageInfo.objects.all()
