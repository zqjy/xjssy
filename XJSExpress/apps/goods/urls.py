from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.goods.views import GoodsInfoViewSet, PriceInfoViewSet, CommentViewSet, GoodsImageViewSet

router = DefaultRouter()
router.register(r'^info', GoodsInfoViewSet, base_name='info')
router.register(r'^comment_info', CommentViewSet, base_name='comment_info')
router.register(r'^goods_img_info', GoodsImageViewSet, base_name='goods_img_info')
get_order = GoodsInfoViewSet.as_view({'get': 'get_order'})
city_wide_create = GoodsInfoViewSet.as_view({"post": 'city_wide_create'})
one_pice_create = GoodsInfoViewSet.as_view({"post": 'one_pice_create'})
the_vehicle_create = GoodsInfoViewSet.as_view({"post": 'the_vehicle_create'})
get_price = PriceInfoViewSet.as_view({'get': 'get_price'})
receive_goods = GoodsInfoViewSet.as_view({'post': 'receive_goods'})
adopt_goods = GoodsInfoViewSet.as_view({'post': 'adopt_goods'})
finish_goods = GoodsInfoViewSet.as_view({'post': 'finish_goods'})
comment_img_upload = CommentViewSet.as_view({'post': 'comment_img_upload'})
customer_comment = CommentViewSet.as_view({'post': 'customer_comment_goods'})
driver_comment = CommentViewSet.as_view({'post': 'driver_comment_goods'})
comment_list = GoodsInfoViewSet.as_view({'get': 'comment_list'})

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
    url(r'^receive/(?P<goods_id>\d+)', receive_goods, name='receive'),  # 接单
    url(r'^adopt/(?P<goods_id>\d+)', adopt_goods, name='adopt'),  # 司机拿到货物
    url(r'^finish/(?P<goods_id>\d+)', finish_goods, name='finish'),  # 完成货单
    url(r'^comment_img_upload', comment_img_upload, name='comment_img_upload'),  # 评论图片上传
    url(r'^driver_comment/(?P<goods_id>\d+)', driver_comment, name='driver_comment'),  # 司机评论
    url(r'^customer_comment/(?P<goods_id>\d+)', customer_comment, name='customer_comment'),  # 顾客评论
    url(r'^get_comment_list[/]?', comment_list, name='get_comment_list'),  # 评论列表
    url(r'^', include(router.urls)),  # Router 方式
]
