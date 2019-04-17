from django.conf.urls import url, include
from apps.area.views import AreaListViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'list', AreaListViewSet, base_name='list')

retrieve_by_name = AreaListViewSet.as_view({'get': 'retrieve_by_name',})
# get_distance = AreaListViewSet.as_view({'get': 'get_distance'})

urlpatterns = [
    url(r'^info/(?P<area_name>\w+)', retrieve_by_name, name='retrieve_by_name'),
    # url(r'^get_distance/(?P<sp_id>\d+)/(?P<sc_id>\d+)/(?P<s_addr>.+)/(?P<dp_id>\d+)/(?P<dc_id>\d+)/(?P<d_addr>.+)',
    #     get_distance, name='get_distance'),  # 获取距离
    url(r'^', include(router.urls)),  # Router 方式
]