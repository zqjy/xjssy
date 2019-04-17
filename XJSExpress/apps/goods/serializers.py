# coding=utf-8
import re, time, math, os

from rest_framework import serializers
from collections import OrderedDict
from datetime import datetime, timedelta
from enum import Enum

from apps.goods.models import GoodsInfo, GoodsCommentImageInfo, GoodsImageInfo
from apps.area.models import Areainfo
from apps.car.models import Carinfo
from apps.driver.models import LoginTokenInfo
from utils import my_utils
from XJSExpress import settings
from db_base.base_model import BaseEnum
from db_base.base_serializers import MyBaseSerializer


class GoodsEnum(Enum):
    """
    货单类型枚举类
    """
    # 货单类型
    CITY_WIDE = 1  # 同城
    ONE_PIECE = 2  # 全国零单
    THE_VEHICLE = 3  # 全国整车
    # 货单运输状态
    NO_TRANSPORT = 1  # 未运输
    IN_TRANSPORT = 2  # 运输中
    YES_TRANSPORT = 3  # 已到达
    # 货物是否提取
    NO_EXTRACT = 0  # 未提取
    YES_EXTRACT = 1  # 已提取
    # 评级级别
    GOOD = 1  # 好评
    MIDDLE = 2  # 中评
    BAD = 3  # 差评
    # 评论图片状态
    Customer = 1  # 顾客评论
    Driver = 2  # 司机评论
    # 订单状态
    NORMAL = 0  # 正常
    DEL = 1  # 删除
    ILLEGAL = 2  # 违规
    CANCEL = 3  # 取消
    # 是否评价
    YES_COMMENT = 1  # 已评论
    NO_COMMENT = 0  # 未评论


class BaseGoodsSerializer(serializers.ModelSerializer):
    """
       货单信息基类
       """
    RET_STR = '请输入'  # 错误信息开头部分

    CustomerId = serializers.IntegerField(write_only=True, help_text='客户ID', label='客户ID',  # 客户合法校验未完成
                                          error_messages={"blank": RET_STR + "客户ID", "required": RET_STR + "客户ID"})
    CarId = serializers.IntegerField(help_text='车辆类型ID', label='车辆类型ID',
                                     error_messages={"blank": RET_STR + "车辆类型ID", "required": RET_STR + "车辆类型ID"})
    GoodsType = serializers.IntegerField(help_text='货单类型', label='货单类型',
                                         error_messages={"blank": RET_STR + "货单类型", "required": RET_STR + "货单类型"})
    GoodsStatus = serializers.IntegerField(read_only=True, help_text='订单状态', label='订单状态')
    GoodsNo = serializers.CharField(read_only=True, help_text='订单编号', label='订单编号')

    SendProvinceId = serializers.IntegerField(help_text='起始地省份ID', label='起始地省份',
                                              error_messages={"blank": RET_STR + "起始地省份",
                                                              "required": RET_STR + "起始地省份"})
    SendCityId = serializers.IntegerField(help_text='起始地城市ID', label='起始地城市',
                                          error_messages={"blank": RET_STR + "起始地城市", "required": RET_STR + "起始地城市"})
    SendDistricId = serializers.IntegerField(help_text='起始地区县ID', label='起始地区县',
                                             error_messages={"blank": RET_STR + "起始地区县", "required": RET_STR + "起始地区县"})
    SendAddress = serializers.CharField(write_only=True, help_text='起始地地址', label='起始地地址',
                                        error_messages={"blank": RET_STR + "起始地地址", "required": RET_STR + "起始地地址"})

    ArriveProvinceId = serializers.IntegerField(read_only=True, help_text='目的地省份ID', label='目的地省份',
                                                error_messages={"blank": RET_STR + "目的地省份",
                                                                "required": RET_STR + "起始地省份"})
    ArriveCityId = serializers.IntegerField(read_only=True, help_text='目的地城市ID', label='目的地城市',
                                            error_messages={"blank": RET_STR + "目的地城市", "required": RET_STR + "目的地城市"})
    ArriveDistricId = serializers.IntegerField(help_text='目的地区县ID', label='目的地区县',
                                               error_messages={"blank": RET_STR + "目的地区县",
                                                               "required": RET_STR + "目的地区县"})
    ArriveAddress = serializers.CharField(write_only=True, help_text='目的地地址', label='目的地地址',
                                          error_messages={"blank": RET_STR + "目的地地址", "required": RET_STR + "目的地地址"})

    PublishName = serializers.CharField(help_text='接收人姓名', label='姓名',
                                        error_messages={"blank": RET_STR + "姓名", "required": RET_STR + "姓名"})
    PublishPhone = serializers.CharField(write_only=True, max_length=11, help_text='接收人电话', label='联系电话',
                                         error_messages={"blank": RET_STR + "联系电话", "required": RET_STR + "联系电话"})
    PublishDate = serializers.DateTimeField(read_only=True, help_text='发布时间', label='发布时间', default=datetime.now())

    KM = serializers.FloatField(read_only=True, required=False, help_text='线路距离', label='公里')
    GoodsFreight = serializers.FloatField(read_only=True, required=False, help_text='货物运费', label='运费')

    PublishRemark = serializers.CharField(read_only=True, help_text='发布声明', label='发布声明')
    CarName = serializers.CharField(read_only=True, help_text='车辆类型', label='车辆类型')
    GoodsName = serializers.CharField(read_only=True, help_text='货单名称', label='货单名称')
    Status = serializers.IntegerField(read_only=True, help_text='数据状态', label='数据状态')
    AddTime = serializers.DateTimeField(read_only=True, help_text='添加时间', label='添加时间', default=datetime.now())
    LastEditTime = serializers.DateTimeField(read_only=True, help_text='最后修改时间', label='最后修改时间', default=datetime.now())

    Grabbing = serializers.DateTimeField(read_only=True, help_text='时间', label='时间', default=datetime.now())
    UnloadingTime = serializers.DateTimeField(read_only=True, help_text='卸货时间', label='卸货时间', default=datetime.now())
    LoadTime = serializers.DateTimeField(read_only=True, help_text='装货时间', label='装货时间', default=datetime.now())
    MakeToOrderDate = serializers.DateTimeField(read_only=True, help_text='接单时间', label='接单时间', default=datetime.now())
    SendX = serializers.CharField(read_only=True, help_text='坐标', label='坐标')
    SendY = serializers.CharField(read_only=True, help_text='坐标', label='坐标')
    ArriveX = serializers.CharField(read_only=True, help_text='坐标', label='坐标')
    ArriveY = serializers.CharField(read_only=True, help_text='坐标', label='坐标')

    # 校验方法
    def validate_CustomerId(self, CustomerId):
        pass

    def validate_PublishPhone(self, PublishPhone):
        if not re.match(settings.REGEX_MOBILE, PublishPhone):
            raise serializers.ValidationError("电话号码非法")
        return PublishPhone

    def validate_GoodsType(self, GoodsType):
        if not GoodsType in [v.value for k, v in GoodsEnum.__members__.items()]:
            raise serializers.ValidationError("订单类型错误")
        return GoodsType

    def validate_SendProvinceId(self, SendProvinceId):
        ret = BaseGoodsSerializer.verify_all_area(provice_id=SendProvinceId, area_type='起始地')
        if not isinstance(ret, str): raise ret
        return SendProvinceId

    def validate_SendCityId(self, SendCityId):
        ret = BaseGoodsSerializer.verify_all_area(provice_id=self.initial_data["SendProvinceId"], city_id=SendCityId,
                                             area_type='起始地')
        if not isinstance(ret, str): raise ret
        return SendCityId

    def validate_SendDistricId(self, SendDistricId):
        ret = BaseGoodsSerializer.verify_all_area(provice_id=self.initial_data["SendProvinceId"],
                                             city_id=self.initial_data["SendCityId"],
                                             distr_id=SendDistricId,
                                             area_type='起始地')
        if not isinstance(ret, str): raise ret
        return SendDistricId

    def validate_ArriveDistricId(self, ArriveDistricId):
        ret = BaseGoodsSerializer.verify_all_area(provice_id=self.initial_data["SendProvinceId"],
                                             city_id=self.initial_data["SendCityId"],
                                             distr_id=ArriveDistricId,
                                             area_type='目的地')
        if not isinstance(ret, str): raise ret
        return ArriveDistricId

    @staticmethod
    def verify_all_area(provice_id, city_id=None, distr_id=None, area_type=''):
        """
        判断省 市 区 id 是否有关联
        :param provice_id:
        :param city_id:
        :param distr_id:
        :param area_type: 检测类型：起始地 | 目的地
        :return:
        """
        if provice_id \
                and not city_id \
                and not distr_id \
                and not BaseGoodsSerializer.verify_area(provice_id, 0):
            raise serializers.ValidationError(area_type + "省份不合法")
        if provice_id \
                and city_id \
                and not distr_id \
                and not BaseGoodsSerializer.verify_area(city_id, provice_id):
            raise serializers.ValidationError(area_type + "城市不匹配")
        if provice_id \
                and city_id \
                and distr_id \
                and not BaseGoodsSerializer.verify_area(distr_id, city_id):
            raise serializers.ValidationError(area_type + "区县不匹配")
        if provice_id \
                and not city_id \
                and distr_id:
            raise serializers.ValidationError("地址数据异常")
        return "ok"

    @staticmethod
    def verify_area(area_id, parent_id):
        """
        判断地区ID是否存在
        :param area_id:
        :param parent_id:
        :return:
        """
        area_info = Areainfo.objects.filter(AreaId=area_id)
        if area_info and area_info[0].ParentId == int(parent_id):
            return area_info[0]
        else:
            return None

    class Meta:
        abstract = True
        model = GoodsInfo
        fields = ('SendProvinceId', 'SendCityId', 'SendDistricId',  # 起始地ID
                  'ArriveProvinceId', 'ArriveCityId', 'ArriveDistricId',  # 到达地ID
                  'PublishDate',  # 下单时间
                  'GoodsType',  # 订单类型
                  'GoodsFreight',  # 9.6  暂时返回价格
                  'KM',  # 距离
                  'CarId',  # 汽车类型ID
                  'CarName',  # 汽车类型
                  'GoodsName',  # 货物名称
                  'PublishRemark',  # 备注
                  'PublishName',  # 接收人名字
                  )


class GoodsInfoSerializer(BaseGoodsSerializer):
    """
    货单信息基类
    """

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # 价格
        try:
            freight = float(data['GoodsFreight'])
        except:
            freight = 0.0
        freight *= 100
        data['GoodsFreight'] = '%.2f' % (math.floor(freight) / 100)  # 小数位舍去
        data['GoodsFreight'] = '%.2f' % (round(freight) / 100)  # 小数位四舍五入
        # 起始地点
        area = Areainfo.objects.filter(AreaId=data['SendProvinceId']).first()
        data['SendProvince'] = area.AreaName if area else ''
        area = Areainfo.objects.filter(AreaId=data['SendCityId']).first()
        data['SendCity'] = area.AreaName if area else ''
        area = Areainfo.objects.filter(AreaId=data['SendDistricId']).first()
        data['SendDistric'] = area.AreaName if area else ''
        # 目的地
        area = Areainfo.objects.filter(AreaId=data['ArriveProvinceId']).first()
        data['ArriveProvince'] = area.AreaName if area else ''
        area = Areainfo.objects.filter(AreaId=data['ArriveCityId']).first()
        data['ArriveCity'] = area.AreaName if area else ''
        area = Areainfo.objects.filter(AreaId=data['ArriveDistricId']).first()
        data['ArriveDistric'] = area.AreaName if area else ''
        # 汽车类型
        car = Carinfo.objects.filter(CarId=data['CarId']).first()
        data['CarName'] = car.CarName if car else ''
        # 发布时间 5分钟以内为"刚刚"
        five_min_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
        publish_date = datetime.strptime(data['PublishDate'], '%Y-%m-%dT%H:%M:%S')
        if publish_date:
            if not publish_date < five_min_ago:
                data['PublishDate'] = '刚刚'
            else:
                data['PublishDate'] = publish_date.strftime("%Y-%m-%d %H:%M:%S")

        # 删除返回字段
        del data['SendProvinceId']
        del data['SendCityId']
        del data['SendDistricId']
        del data['ArriveProvinceId']
        del data['ArriveCityId']
        del data['ArriveDistricId']
        del data['CarId']
        return data


class CityWideSerializer(BaseGoodsSerializer):
    """
    同城货单
    """
    # RET_STR = '请输入'  # 错误信息开头部分
    GoodsType = serializers.IntegerField(read_only=True, help_text='货单类型', label='货单类型',
                                         error_messages={"blank": BaseGoodsSerializer.RET_STR + "货单类型",
                                                         "required": BaseGoodsSerializer.RET_STR + "货单类型"})
    SendAddress = serializers.CharField(help_text='起始地地址', label='起始地地址',
                                        error_messages={"blank": BaseGoodsSerializer.RET_STR + "起始地地址",
                                                        "required": BaseGoodsSerializer.RET_STR + "起始地地址"})
    ArriveAddress = serializers.CharField(help_text='目的地地址', label='目的地地址',
                                          error_messages={"blank": BaseGoodsSerializer.RET_STR + "目的地地址",
                                                          "required": BaseGoodsSerializer.RET_STR + "目的地地址"})
    PublishName = serializers.CharField(help_text='接收人姓名', label='姓名',
                                        error_messages={"blank": BaseGoodsSerializer.RET_STR + "姓名",
                                                        "required": BaseGoodsSerializer.RET_STR + "姓名"})
    PublishPhone = serializers.CharField(max_length=11, help_text='接收人电话', label='联系电话',
                                         error_messages={"blank": BaseGoodsSerializer.RET_STR + "联系电话",
                                                         "required": BaseGoodsSerializer.RET_STR + "联系电话"})

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['GoodsType'] = GoodsEnum.CITY_WIDE.value
    #     # 价格
    #     try:
    #         freight = float(data['GoodsFreight'])
    #     except:
    #         freight = 0.0
    #     freight *= 100
    #     data['GoodsFreight'] = '%.2f' % (math.floor(freight) / 100)  # 小数位舍去
    #     data['GoodsFreight'] = '%.2f' % (round(freight) / 100)  # 小数位四舍五入
    #     data['ArriveProvinceId'] = data['SendProvinceId']
    #     data['ArriveCityId'] = data['SendCityId']
    #     # 汽车类型
    #     car = Carinfo.objects.filter(CarId=data['CarId']).first()
    #     data['CarName'] = car.CarName if car else ''
    #     # 额外字段
    #     data['AddTime'] = datetime.now()  # 添加时间
    #     data['LastEditTime'] = datetime.now()  # 最后修改时间
    #     data['PublishDate'] = datetime.now()  # 发布时间
    #     return data

    def validate(self, attrs):
        keys = attrs.keys()

        # 订单类型
        attrs['GoodsType'] = GoodsEnum.CITY_WIDE.value
        # 订单状态
        attrs['GoodsStatus'] = GoodsEnum.NO_TRANSPORT.value
        # 订单编号
        attrs['GoodsNo'] = re.sub(r'[-|\s+|:\.]', '', str(datetime.now()))[:15]
        # 目的地
        if not 'ArriveProvinceId' in keys or not 'ArriveCityId' in keys or not attrs['ArriveProvinceId'] or not attrs[
            'ArriveCityId']:
            attrs['ArriveProvinceId'] = attrs['SendProvinceId']
            attrs['ArriveCityId'] = attrs['SendCityId']
        # 汽车类型
        if 'CarId' in keys and not attrs['CarId']:
            car = Carinfo.objects.filter(CarId=attrs['CarId']).first()
            attrs['CarName'] = car.CarName if car else ''
        # 时间
        attrs['AddTime'] = datetime.now()  # 添加时间
        attrs['LastEditTime'] = datetime.now()  # 最后修改时间
        attrs['PublishDate'] = datetime.now()  # 发布时间
        # 发布订单不包含以下字段
        if not 'Grabbing' in keys or not attrs['Grabbing']:
            attrs['Grabbing'] = attrs['PublishDate'] - timedelta(hours=1)  # 不知道什么字段
        if not 'UnloadingTime' in keys or not attrs['UnloadingTime']:
            attrs['UnloadingTime'] = attrs['PublishDate'] - timedelta(hours=1)  # 卸货时间
        if not 'LoadTime' in keys or not attrs['LoadTime']:
            attrs['LoadTime'] = attrs['PublishDate'] - timedelta(hours=1)  # 装车时间
        if not 'MakeToOrderDate' in keys or not attrs['MakeToOrderDate']:
            attrs['MakeToOrderDate'] = attrs['PublishDate'] - timedelta(hours=1)  # 接单时间
        # 数据状态
        attrs['Status'] = BaseEnum.NORMAL.value
        # 公里数
        if 'CarId' not in keys:
            o_dict = my_utils.get_price_static(1, 1,
                                                   attrs['SendProvinceId'], attrs['SendCityId'], attrs['SendAddress'],
                                                   attrs['ArriveProvinceId'], attrs['ArriveCityId'],
                                                   attrs['ArriveAddress'], 0.0, 0.0)
        else:
            o_dict = my_utils.get_price_static(attrs['CarId'], 1,
                                               attrs['SendProvinceId'], attrs['SendCityId'], attrs['SendAddress'],
                                               attrs['ArriveProvinceId'], attrs['ArriveCityId'],
                                               attrs['ArriveAddress'], 0.0, 0.0)

        if not o_dict.data.get('Success'):
            raise serializers.ValidationError('获取公里数失败: '+ str(o_dict))
        # print('*' * 20, o_dict.data)
        km = o_dict.data.get('Data')[0].get('distance_value')/1000
        freight = o_dict.data.get('Data')[0].get('price')
        # print('*'*20,o_dict.data, km, freight)
        attrs['KM'] = km
        # 运费
        if 'CarId' in keys:
            attrs['GoodsFreight'] = freight
        # 坐标
        attrs['SendX'] = o_dict.data.get('Data')[0].get('send_x')
        attrs['SendY'] = o_dict.data.get('Data')[0].get('send_y')
        attrs['ArriveX'] = o_dict.data.get('Data')[0].get('arrive_x')
        attrs['ArriveY'] = o_dict.data.get('Data')[0].get('arrive_y')
        return attrs

    class Meta:
        model = BaseGoodsSerializer.Meta.model
        fields = BaseGoodsSerializer.Meta.fields + ('PublishPhone',  # 接收人电话
                                               'SendAddress',  # 起始地详细地址
                                               'ArriveAddress',  # 目的地地址
                                               'AddTime',  # 添加时间
                                               'LastEditTime',  # 最后修改时间
                                               'PublishDate',  # 发布时间
                                               'GoodsStatus',  # 订单状态
                                               'GoodsNo',  # 订单编号
                                               'SendX',
                                               'SendY',
                                               'ArriveX',
                                               'ArriveY',
                                               )


class OnePieceSerializer(CityWideSerializer):
    """
    全国零单
    """

    SendAddress = serializers.CharField(help_text='起始地地址', label='货物地址',
                                        error_messages={"blank": BaseGoodsSerializer.RET_STR + "货物地址",
                                                        "required": BaseGoodsSerializer.RET_STR + "货物地址"})
    GoodsName = serializers.CharField(help_text='货物名称', label='货物名称',
                                      error_messages={"blank": BaseGoodsSerializer.RET_STR + "货物名称",
                                                      "required": BaseGoodsSerializer.RET_STR + "货物名称"})
    Weight = serializers.FloatField(help_text='重量(KG)', label='重量(KG)',
                                    error_messages={"blank": BaseGoodsSerializer.RET_STR + "重量",
                                                    "required": BaseGoodsSerializer.RET_STR + "重量"})
    Volume = serializers.FloatField(help_text='体积(方)', label='体积(方)',
                                    error_messages={"blank": BaseGoodsSerializer.RET_STR + "体积",
                                                    "required": BaseGoodsSerializer.RET_STR + "体积"})
    PublishRemark = serializers.CharField(required=False, help_text='备注', label='备注', default='',
                                          error_messages={"blank": BaseGoodsSerializer.RET_STR + "备注",
                                                          "required": BaseGoodsSerializer.RET_STR + "备注"})
    ArriveProvinceId = serializers.IntegerField(help_text='目的地省份ID', label='目的地省份',
                                                error_messages={"blank": BaseGoodsSerializer.RET_STR + "目的地省份",
                                                                "required": BaseGoodsSerializer.RET_STR + "起始地省份"})
    ArriveCityId = serializers.IntegerField(help_text='目的地城市ID', label='目的地城市',
                                            error_messages={"blank": BaseGoodsSerializer.RET_STR + "目的地城市",
                                                            "required": BaseGoodsSerializer.RET_STR + "目的地城市"})
    ArriveAddress = serializers.CharField(help_text='目的地地址', label='卸货地址',
                                          error_messages={"blank": BaseGoodsSerializer.RET_STR + "卸货地址",
                                                          "required": BaseGoodsSerializer.RET_STR + "卸货地址"})
    UnloadingTime = serializers.DateField(help_text='卸货时间', label='卸货时间',
                                          error_messages={"blank": BaseGoodsSerializer.RET_STR + "卸货时间",
                                                          "required": BaseGoodsSerializer.RET_STR + "卸货时间"})

    def validate_ArriveProvinceId(self, ArriveProvinceId):
        ret = BaseGoodsSerializer.verify_all_area(provice_id=ArriveProvinceId, area_type='目的地')
        if not isinstance(ret, str): raise ret
        return ArriveProvinceId

    def validate_ArriveCityId(self, ArriveCityId):
        ret = BaseGoodsSerializer.verify_all_area(provice_id=self.initial_data["ArriveProvinceId"], city_id=ArriveCityId,
                                             area_type='目的地')
        if not isinstance(ret, str): raise ret
        return ArriveCityId

    def validate_ArriveDistricId(self, ArriveDistricId):
        ret = BaseGoodsSerializer.verify_all_area(provice_id=self.initial_data["ArriveProvinceId"],
                                             city_id=self.initial_data["ArriveCityId"],
                                             distr_id=ArriveDistricId,
                                             area_type='目的地')
        if not isinstance(ret, str): raise ret
        return ArriveDistricId

    def validate(self, attrs):
        attrs_new = super().validate(attrs)
        attrs_new['GoodsType'] = GoodsEnum.ONE_PIECE.value
        # 公里数
        if 'CarId' not in attrs.keys():
            o_dict = my_utils.get_price_static(1, 1,
                                                   attrs['SendProvinceId'], attrs['SendCityId'], attrs['SendAddress'],
                                                   attrs['ArriveProvinceId'], attrs['ArriveCityId'],
                                                   attrs['ArriveAddress'], 0.0, 0.0)
        else:
            o_dict = my_utils.get_price_static(attrs['CarId'], 1,
                                               attrs['SendProvinceId'], attrs['SendCityId'], attrs['SendAddress'],
                                               attrs['ArriveProvinceId'], attrs['ArriveCityId'],
                                               attrs['ArriveAddress'], 0.0, 0.0)

        if not o_dict.data.get('Success'):
            raise serializers.ValidationError('获取公里数失败: '+ str(o_dict))
        attrs['KM'] = float(o_dict.data.get('Data')[0].get('distance_value'))/1000
        # 运费
        if 'CarId' in attrs.keys():
            attrs['GoodsFreight'] = o_dict.data.get('Data')[0].get('price')
        return attrs_new

    class Meta:
        model = BaseGoodsSerializer.Meta.model
        fields = CityWideSerializer.Meta.fields + ('GoodsName',  # 货物名称
                                                   'Weight',  # 重量
                                                   'Volume',  # 体积
                                                   'PublishRemark',  # 备注
                                                   'UnloadingTime',  # 卸货时间
                                                   )


class TheVehicleSerializer(OnePieceSerializer):
    """
    全国整车
    """
    IMG_URL = ''  # 图片路径

    CarId = serializers.IntegerField(required=False, read_only=True, help_text='车辆类型ID', label='车辆类型ID', default=0)
    CarName = serializers.CharField(required=False, help_text='车辆类型名称，非必填', label='车辆类型', default='')
    # GoodsImg = serializers.ImageField(write_only=True, required=False, help_text='货物图片', label='货物图片')
    GoodsFreight = serializers.FloatField(help_text='运费', label='运费',
                                          error_messages={"blank": BaseGoodsSerializer.RET_STR + "运费",
                                                          "required": BaseGoodsSerializer.RET_STR + "运费"})
    KM = serializers.FloatField(required=False, read_only=True, help_text='线路距离', label='公里')
    Volume = serializers.FloatField(required=False, read_only=True, help_text='体积(方)', label='体积(方)',
                                    error_messages={"blank": BaseGoodsSerializer.RET_STR + "体积",
                                                    "required": BaseGoodsSerializer.RET_STR + "体积"})

    def validate(self, attrs):
        price = attrs['GoodsFreight']
        attrs_new = super().validate(attrs)
        attrs_new['GoodsType'] = GoodsEnum.THE_VEHICLE.value
        # 公里数

        # 运费
        attrs_new['GoodsFreight'] = price
        return attrs_new

    class Meta:
        model = BaseGoodsSerializer.Meta.model
        fields = OnePieceSerializer.Meta.fields


class ReceiveSerializer(serializers.ModelSerializer):
    tokenId = serializers.CharField(write_only=True, help_text='token', label='token',
                                         error_messages={"blank": BaseGoodsSerializer.RET_STR + "token",
                                                         "required": BaseGoodsSerializer.RET_STR + "token"})

    UnloadingTime = serializers.DateTimeField(read_only=True, help_text='卸货时间', label='卸货时间')
    MakeToOrderDate = serializers.DateTimeField(read_only=True, help_text='接单时间', label='接单时间')
    PublishDate = serializers.DateTimeField(read_only=True, help_text='发布时间', label='发布时间')
    LastEditTime = serializers.DateTimeField(read_only=True, help_text='最后修改时间', label='最后修改时间')
    LoadTime = serializers.DateTimeField(read_only=True, help_text='装货时间', label='装货时间')
    Grabbing = serializers.DateTimeField(read_only=True, help_text='时间', label='时间')
    AddTime = serializers.DateTimeField(read_only=True, help_text='添加时间', label='添加时间')

    def validate_tokenId(self, tokenId):
        token_info = LoginTokenInfo.objects.filter(LoginToken=tokenId).first()
        if not token_info: raise serializers.ValidationError("无权限")
        return token_info

    def validate(self, attrs):
        attrs["DriverId"] = attrs["tokenId"].DriverId
        attrs["MakeToOrderDate"] = datetime.now()
        attrs["LastEditTime"] = datetime.now()
        del attrs['tokenId']
        return attrs

    class Meta:
        model = GoodsInfo
        fields = ('tokenId', 'DriverId', 'MakeToOrderDate', 'LastEditTime',
                  'UnloadingTime', 'PublishDate', 'LoadTime', 'Grabbing', 'AddTime')


class AdoptSerializer(ReceiveSerializer):
    def validate(self, attrs):
        attrs["GoodsStatus"] = GoodsEnum.IN_TRANSPORT.value
        attrs["LastEditTime"] = datetime.now()
        del attrs['tokenId']
        return attrs


class FinishSerializer(serializers.ModelSerializer):
    UnloadingTime = serializers.DateTimeField(read_only=True, help_text='卸货时间', label='卸货时间')
    MakeToOrderDate = serializers.DateTimeField(read_only=True, help_text='接单时间', label='接单时间')
    PublishDate = serializers.DateTimeField(read_only=True, help_text='发布时间', label='发布时间')
    LastEditTime = serializers.DateTimeField(read_only=True, help_text='最后修改时间', label='最后修改时间')
    LoadTime = serializers.DateTimeField(read_only=True, help_text='装货时间', label='装货时间')
    Grabbing = serializers.DateTimeField(read_only=True, help_text='时间', label='时间')
    AddTime = serializers.DateTimeField(read_only=True, help_text='添加时间', label='添加时间')


    def validate(self, attrs):
        attrs['GoodsStatus'] = 3
        attrs["UnloadingTime"] = datetime.now()
        attrs["LastEditTime"] = datetime.now()
        return attrs

    class Meta:
        model = GoodsInfo
        fields = ('DriverId', 'MakeToOrderDate', 'LastEditTime',
                  'UnloadingTime', 'PublishDate', 'LoadTime', 'Grabbing', 'AddTime')


class DriverCommentSerializer(serializers.ModelSerializer):
    """
    司机评价订单
    """
    tokenId = serializers.CharField(write_only=True, help_text='token', label='token',
                                    error_messages={"blank": BaseGoodsSerializer.RET_STR + "token",
                                                    "required": BaseGoodsSerializer.RET_STR + "token"})
    D_CommentContent = serializers.CharField(help_text='司机评论内容', label='司机评论内容',
                                             error_messages={"blank": BaseGoodsSerializer.RET_STR + "评论内容",
                                                             "required": BaseGoodsSerializer.RET_STR + "评论内容"})
    D_CommentScore = serializers.IntegerField(help_text='司机评分', label='司机评分',
                                              error_messages={"blank": BaseGoodsSerializer.RET_STR + "司机评分",
                                                              "required": BaseGoodsSerializer.RET_STR + "司机评分"})
    D_IsComment = serializers.IntegerField(read_only=True, help_text='司机是否评论', label='司机是否评论')



    UnloadingTime = serializers.DateTimeField(read_only=True, help_text='卸货时间', label='卸货时间')
    MakeToOrderDate = serializers.DateTimeField(read_only=True, help_text='接单时间', label='接单时间')
    PublishDate = serializers.DateTimeField(read_only=True, help_text='发布时间', label='发布时间')
    LastEditTime = serializers.DateTimeField(read_only=True, help_text='最后修改时间', label='最后修改时间')
    LoadTime = serializers.DateTimeField(read_only=True, help_text='装货时间', label='装货时间')
    Grabbing = serializers.DateTimeField(read_only=True, help_text='时间', label='时间')
    AddTime = serializers.DateTimeField(read_only=True, help_text='添加时间', label='添加时间')

    def validate_tokenId(self, tokenId):
        token_info = LoginTokenInfo.objects.filter(LoginToken=tokenId).first()
        if not token_info: raise serializers.ValidationError("无权限")
        return token_info

    def validate_D_CommentScore(self, D_CommentScore):
        if not D_CommentScore in [1, 2, 3]: raise serializers.ValidationError('评分错误')
        return D_CommentScore

    def validate(self, attrs):
        attrs['D_IsComment'] = GoodsEnum.YES_COMMENT.value
        attrs["LastEditTime"] = datetime.now()
        del attrs['tokenId']
        return attrs

    class Meta:
        model = GoodsInfo
        fields = ('tokenId', 'MakeToOrderDate', 'LastEditTime',
                  'UnloadingTime', 'PublishDate', 'LoadTime', 'Grabbing', 'AddTime',
                  'D_IsComment', 'D_CommentContent', 'D_CommentScore')


class CustomerCommentSerializer(serializers.ModelSerializer):
    """
    顾客评价订单
    """
    tokenId = serializers.CharField(write_only=True, help_text='token', label='token',
                                    error_messages={"blank": BaseGoodsSerializer.RET_STR + "token",
                                                    "required": BaseGoodsSerializer.RET_STR + "token"})
    C_CommentContent = serializers.CharField(help_text='顾客评论内容', label='顾客评论内容',
                                             error_messages={"blank": BaseGoodsSerializer.RET_STR + "评论内容",
                                                             "required": BaseGoodsSerializer.RET_STR + "评论内容"})
    C_CommentScore = serializers.IntegerField(help_text='顾客评分', label='顾客评分',
                                              error_messages={"blank": BaseGoodsSerializer.RET_STR + "顾客评分",
                                                              "required": BaseGoodsSerializer.RET_STR + "顾客评分"})
    C_IsComment = serializers.IntegerField(read_only=True, help_text='顾客是否评论', label='顾客是否评论')



    UnloadingTime = serializers.DateTimeField(read_only=True, help_text='卸货时间', label='卸货时间')
    MakeToOrderDate = serializers.DateTimeField(read_only=True, help_text='接单时间', label='接单时间')
    PublishDate = serializers.DateTimeField(read_only=True, help_text='发布时间', label='发布时间')
    LastEditTime = serializers.DateTimeField(read_only=True, help_text='最后修改时间', label='最后修改时间')
    LoadTime = serializers.DateTimeField(read_only=True, help_text='装货时间', label='装货时间')
    Grabbing = serializers.DateTimeField(read_only=True, help_text='时间', label='时间')
    AddTime = serializers.DateTimeField(read_only=True, help_text='添加时间', label='添加时间')

    def validate_tokenId(self, tokenId):
        token_info = LoginTokenInfo.objects.filter(LoginToken=tokenId).first()
        # if not token_info: raise serializers.ValidationError("无权限")
        return token_info

    def validate_C_CommentScore(self, C_CommentScore):
        if not C_CommentScore in [1, 2, 3]: raise serializers.ValidationError('评分错误')
        return C_CommentScore

    def validate(self, attrs):
        attrs['C_IsComment'] = GoodsEnum.YES_COMMENT.value
        attrs["LastEditTime"] = datetime.now()
        del attrs['tokenId']
        return attrs

    class Meta:
        model = GoodsInfo
        fields = ('tokenId', 'MakeToOrderDate', 'LastEditTime',
                  'UnloadingTime', 'PublishDate', 'LoadTime', 'Grabbing', 'AddTime',
                  'C_IsComment', 'C_CommentContent', 'C_CommentScore')


class CommentSerializer(serializers.ModelSerializer):
    """
    评价订单
    """

    class Meta:
        model = GoodsInfo
        fields = '__all__'


class CommentImageSerializer(MyBaseSerializer):
    """
    评论图片上传
    """
    Type = serializers.IntegerField(help_text='评论类型', label='评论类型')
    GoodsId = serializers.IntegerField(help_text='货单ID', label='货单ID')
    ImageUrl = serializers.ImageField(required=False, help_text='图片', label='图片')
    IsCheck = serializers.IntegerField(read_only=True, help_text='是否审核', label='是否审核')

    def validate_Type(self, Type):
        if not Type in [1, 2]:
            raise serializers.ValidationError("评论类型错误")
        return Type

    def validate_GoodsId(self, GoodsId):
        goods_info = GoodsInfo.objects.filter(GoodsId=GoodsId).first()
        if not goods_info:
            raise serializers.ValidationError("订单ID错误")
        return GoodsId

    class Meta:
        model = GoodsCommentImageInfo
        fields = '__all__'


class GoodsImgSerializer(MyBaseSerializer):
    """
    订单图片
    """
    GoodsId = serializers.CharField(help_text='订单ID', label='订单ID',
                                    error_messages={"blank": "订单ID为必填", "required": "订单ID为必填"})
    ImageUrl = serializers.ImageField(help_text='图片', label='图片',
                                      error_messages={"blank": "图片为必填", "required": "图片为必填"})
    IsCover = serializers.IntegerField(required=False, help_text='是否封面', label='是否封面')

    def validate_GoodsId(self, GoodsId):
        goods_info = GoodsInfo.objects.filter(GoodsId=GoodsId).first()
        if not goods_info: raise serializers.ValidationError('订单ID异常')
        return GoodsId

    def validate(self, attrs):
        if 'IsCover' in attrs.keys() and not attrs['IsCover']: attrs['IsCover'] = 0
        attrs['AddTime'] = datetime.now()
        attrs['LastEditTime'] = datetime.now()
        return attrs

    def create(self, validated_data):
        goods_info = GoodsInfo.objects.filter(GoodsId=validated_data['GoodsId']).first()
        save_path = my_utils.upload_img(validated_data, 'ImageUrl', 'goods/' + goods_info.GoodsNo + '/')
        if save_path and not isinstance(save_path, str):
            raise serializers.ValidationError('图片保存失败')

        validated_data['ImageUrl'] = save_path
        goods_img_info = GoodsImageInfo.objects.create(**validated_data)
        return goods_img_info

    class Meta:
        model = GoodsImageInfo
        fields = '__all__'

