import json, math, hashlib, requests
from rest_framework import status
from rest_framework.response import Response

from apps.goods.models import KmPriceInfo
from apps.area.models import Areainfo
from utils import my_reponse

def md5(str):
    """
    MD5加密
    :param str:
    :return:
    """
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()

def get_distance(sp_id, sc_id, s_addr, dp_id, dc_id, d_addr):
        """
        获取两地距离
        :param request:
        :param sp_id: 起始地省份ID
        :param sc_id: 起始地市ID
        :param s_addr: 起始地详细地址
        :param dp_id: 目的地省份ID
        :param dc_id: 目的地市ID
        :param d_addr: 目的地详细地址
        :return: 距离
        """
        # 参数校验
        sp_info = Areainfo.objects.filter(AreaId=sp_id).first()
        dp_info = Areainfo.objects.filter(AreaId=dp_id).first()
        if not sp_info or not dp_info:
            return Response(my_reponse.get_response_error_dict(msg='参数错误'), status=status.HTTP_400_BAD_REQUEST)

        sc_info = Areainfo.objects.filter(AreaId=sc_id).first()
        dc_info = Areainfo.objects.filter(AreaId=dc_id).first()
        if not sc_info \
                or not dc_info \
                or sc_info.ParentId != int(sp_id) \
                or dc_info.ParentId != int(dp_id):
            return Response(my_reponse.get_response_error_dict(msg='参数错误'), status=status.HTTP_400_BAD_REQUEST)

        # 获取经纬度地址
        start_url = 'http://api.map.baidu.com/geocoder/v2/?address=%s' \
                    '&output=json' \
                    '&ak=990ca087457a9923cc7fd20bbb45b6b9'

        s_address = sp_info.AreaName + sc_info.AreaName + s_addr
        d_address = dp_info.AreaName + dc_info.AreaName + d_addr

        # 获取起始地经纬度
        resp = requests.get(start_url % s_address)
        s_json_str = resp.content.decode(encoding='utf-8')
        s_json = json.loads(s_json_str)
        # print('*'*10, s_json_str)
        # {"status":0,"result":{"location":{"lng":119.27516126752177,"lat":26.11533247623715},"precise":1,"confidence":70,"comprehension":100,"level":"UNKNOWN"}}

        # 获取目标地经纬度
        resp = requests.get(start_url % d_address)
        d_json_str = resp.content.decode(encoding='utf-8')
        d_json = json.loads(d_json_str)

        if s_json.get('status') != 0 or d_json.get('status') != 0:
            return Response(my_reponse.get_response_error_dict(msg='获取经纬度失败，请稍后重试'),
                            status=status.HTTP_408_REQUEST_TIMEOUT)

        # 经纬度获取
        url_map = {
            'ori_lat_1': s_json.get('result').get('location').get('lat'),
            'ori_lng_1': s_json.get('result').get('location').get('lng'),
            # 'ori_lat_2': s_json.get('result').get('location').get('lat'),
            # 'ori_lng_2': s_json.get('result').get('location').get('lng'),
            'des_lat_1': d_json.get('result').get('location').get('lat'),
            'des_lng_1': d_json.get('result').get('location').get('lng'),
            # 'des_lat_2': d_json.get('result').get('location').get('lat'),
            # 'des_lng_2': d_json.get('result').get('location').get('lng')
        }

        # 获取距离地址
        # distance_url = 'http://api.map.baidu.com/routematrix/v2/driving?output=json' \
        #                '&origins={ori_lat_1},{ori_lng_1}|{ori_lat_2},{ori_lng_2}' \
        #                '&destinations={des_lat_1},{des_lng_1}|{des_lat_2},{des_lng_2}' \
        #                '&ak=990ca087457a9923cc7fd20bbb45b6b9'
        distance_url = 'http://api.map.baidu.com/routematrix/v2/driving?output=json' \
                       '&origins={ori_lat_1},{ori_lng_1}' \
                       '&destinations={des_lat_1},{des_lng_1}' \
                       '&ak=VdIYG885wGKdqCeERz4ICIQDSvaM64Y9'

        distance_url = distance_url.format(**url_map)
        # print('*'*20, distance_url)

        resp = requests.get(distance_url)
        # print('*' * 20, resp.content.decode(encoding='utf-8'))
        # {"status":0,"result":[{"distance":{"text":"1.2公里","value":1184},"duration":{"text":"1分钟","value":44}}],"message":"成功"}

        distance_json = resp.json()
        if distance_json.get('status') != 0:
            return Response(my_reponse.get_response_error_dict(msg='获取距离，请稍后重试'),
                            status=status.HTTP_408_REQUEST_TIMEOUT)

        res_json = distance_json.get('result')[0]
        res_json['send_x'] = url_map['ori_lat_1']
        res_json['send_y'] = url_map['ori_lng_1']
        res_json['arrive_x'] = url_map['des_lat_1']
        res_json['arrive_y'] = url_map['des_lng_1']
        return Response(my_reponse.get_response_dict(res_json), status=status.HTTP_200_OK)

def get_price_static(car_id, type, sp_id, sc_id, s_addr, dp_id, dc_id, d_addr, weight=0.0, volume=0.0):
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
        # 数据校验
        if int(type) != 1 and int(type) !=2:
            return Response(my_reponse.get_response_error_dict('订单类型错误'), status=status.HTTP_400_BAD_REQUEST)

        # 获取距离
        ret = get_distance(sp_id, sc_id, s_addr, dp_id, dc_id, d_addr)
        # print(ret.data)
        # ret_json = json.loads(ret.data)
        if not ret.data.get('Success'):
            return Response(ret.data, status=status.HTTP_400_BAD_REQUEST)

        d_value = ret.data.get('Data')[0].get('distance').get('value')
        d_text = ret.data.get('Data')[0].get('distance').get('text')
        send_x = ret.data.get('Data')[0].get('send_x')
        send_y = ret.data.get('Data')[0].get('send_y')
        arrive_x = ret.data.get('Data')[0].get('arrive_x')
        arrive_y = ret.data.get('Data')[0].get('arrive_y')

        if not d_value:
            return Response(my_reponse.get_response_error_dict('距离获取失败'), status=status.HTTP_400_BAD_REQUEST)

        # 获取价格 KmPriceType 1:同城 2:全国零单

        price_info = KmPriceInfo.objects.filter(CarId=int(car_id), KmPriceType=int(type)).first()

        if not price_info:
            return Response(my_reponse.get_response_error_dict(msg='车辆类型错误'), status=status.HTTP_400_BAD_REQUEST)

        price = 0.0

        # 起步价
        price = price_func(price, float(d_value)/1000,
                                             price_info.StartKm, price_info.StartKmPrice,
                                             price_info.ExceedStartKm, price_info.ExceedStartKmPrice)
        # 重量价
        if weight and float(weight) > 0:
            price = price_func(price, float(weight),
                                                 price_info.StartWeight, price_info.StartWeightPrice,
                                                 price_info.ExceedStartWeight, price_info.ExceedStartWeightPrice)
        # 体积价
        if volume and float(volume) > 0:
            price = price_func(price, float(volume),
                                                 price_info.StartVolume, price_info.StartVolumePrice,
                                                 price_info.ExceedVolume, price_info.ExceedVolumePrice)

        # print('*'*20, price)

        return Response(my_reponse.get_response_dict({'price': price,
                                                      'distance_value': d_value,
                                                      'distance_text': d_text,
                                                      'send_x': send_x,
                                                      'send_y': send_y,
                                                      'arrive_x': arrive_x,
                                                      'arrive_y': arrive_y}), status=status.HTTP_200_OK)

def price_func(price, value, start, start_price, exceed, exceed_price):
        # print('*' * 20, value, start, start_price, exceed, exceed_price)
        if not float(value)>0: return 0

        if value <= start:
            price += start_price
        else:
            price += start_price + math.ceil((value - start) / exceed) * exceed_price
        # print(price)
        return price

