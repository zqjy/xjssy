from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.goods.views import GoodsInfoViewSet


router = DefaultRouter()
router.register(r'info', GoodsInfoViewSet, base_name='info')
get_order = GoodsInfoViewSet.as_view({'get': 'get_order'})
city_wide_create = GoodsInfoViewSet.as_view({"post": 'city_wide_create'})
one_pice_create = GoodsInfoViewSet.as_view({"post": 'one_pice_create'})
the_vehicle_create = GoodsInfoViewSet.as_view({"post": 'the_vehicle_create'})
urlpatterns = [
    url(r'^city_wide_create', city_wide_create, name='city_wide_create'), # 同城货单
    url(r'^one_pice_create', one_pice_create, name='one_pice_create'), # 全国零单
    url(r'^the_vehicle_create', the_vehicle_create, name='the_vehicle_create'), # 全国整车
    url(r'^get_order', get_order, name='get_order'), # 司机获取个人订单
    url(r'^', include(router.urls)),  # Router 方式
]