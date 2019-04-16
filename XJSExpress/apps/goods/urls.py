from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.goods.views import GoodsInfoViewSet, PriceInfoViewSet

router = DefaultRouter()
router.register(r'info', GoodsInfoViewSet, base_name='info')
get_order = GoodsInfoViewSet.as_view({'get': 'get_order'})
city_wide_create = GoodsInfoViewSet.as_view({"post": 'city_wide_create'})
one_pice_create = GoodsInfoViewSet.as_view({"post": 'one_pice_create'})
the_vehicle_create = GoodsInfoViewSet.as_view({"post": 'the_vehicle_create'})
get_price = PriceInfoViewSet.as_view({'get': 'get_price'})
receive_goods = GoodsInfoViewSet.as_view({'post': 'receive_goods'})
verify_goods = GoodsInfoViewSet.as_view({'post': 'verify_goods'})

urlpatterns = [
    url(r'^get_price/(?P<car_id>\d+)/(?P<type>\d+)/'
        r'(?P<sp_id>\d+)/(?P<sc_id>\d+)/(?P<s_addr>.+)/(?P<dp_id>\d+)/(?P<dc_id>\d+)/(?P<d_addr>.+)'
        r'/(?P<weight>\d?[.]?\d+)/(?P<volume>\d?[.]?\d+)$',
        get_price, name='get_price2'),  # 获取订单价格
    url(r'^get_price/(?P<car_id>\d+)/(?P<type>\d+)/'
        r'(?P<sp_id>\d+)/(?P<sc_id>\d+)/(?P<s_addr>.+)/(?P<dp_id>\d+)/(?P<dc_id>\d+)/(?P<d_addr>.+)$',
        get_price, name='get_price1'),  # 获取订单价格
    url(r'^city_wide_create', city_wide_create, name='city_wide_create'),  # 同城货单
    url(r'^one_pice_create', one_pice_create, name='one_pice_create'),  # 全国零单
    url(r'^the_vehicle_create', the_vehicle_create, name='the_vehicle_create'),  # 全国整车
    url(r'^get_order', get_order, name='get_order'),  # 司机获取个人订单
    url(r'^receive_goods/(?P<goods_id>\d+)', receive_goods, name='receive_goods'),  # 接单
    url(r'^verify_goods/(?P<goods_id>\d+)', verify_goods, name='verify_goods'),  # 接单
    url(r'^', include(router.urls)),  # Router 方式
]
